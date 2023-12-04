#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

int is_json_str(const char *str) {
    size_t len = strlen(str);

    return !(str[0] != '{' && str[len - 2] != '}');
}

PyObject *build_key(const char *token) {
    if (!(token[0] == '\"' && token[strlen(token) - 1] == '\"')) {
        return NULL;
    }

    size_t len = strlen(token);

    char str[len - 1];
    strncpy(str, token + 1, len - 2);
    str[len - 2] = '\0';

    return Py_BuildValue("s", str);
}

PyObject *build_value(const char *token) {
    size_t len = strlen(token);

    if (!(token[0] == '\"' && token[len - 1] == '\"')) {
        for (size_t i = 0; i < len; i++) {
            if (!isdigit(token[i])) {
                return NULL;
            }
        }
        return Py_BuildValue("i", atoi(token));
    }

    char str[len - 1];
    strncpy(str, token + 1, len - 2);
    str[len - 2] = '\0';

    return Py_BuildValue("s", str);
}

PyObject *cjson_loads(PyObject *self, PyObject *args) {

    char *argument_str = NULL;
    if (!PyArg_ParseTuple(args, "s", &argument_str)) {
        PyErr_Format(PyExc_TypeError, "Expected object or value");
        return NULL;
    }

    if (!is_json_str(argument_str)) {
        PyErr_Format(PyExc_TypeError, "Expected object or value");
    }

    size_t len = strlen(argument_str);

    char json_string[len - 2];
    strncpy(json_string, argument_str + 1, len - 2);
    json_string[len - 2] = '\0';

    PyObject *dict = NULL;
    if (!(dict = PyDict_New())) {
        printf("ERROR: Failed to create Dict Object\n");
        return NULL;
    }

    char* token = strtok(json_string, ":, ");

    PyObject *key = NULL;
    PyObject *value = NULL;
    while (token != NULL) {
        if (!key) {
            key = build_key(token);

            if (!key) {
                PyErr_Format(PyExc_TypeError, "ERROR: Failed to build key\n");
                return NULL;
            }

        } else {
             value = build_value(token);

            if (!value) {
                PyErr_Format(PyExc_TypeError, "ERROR: Failed to build value\n");
                return NULL;
            }

            if (PyDict_SetItem(dict, key, value) < 0) {
                printf("ERROR: Failed to set item\n");
                return NULL;
            }

            key = NULL;
            value = NULL;
        }
        token = strtok(NULL, ":, ");
    }

    return dict;
}

int check_dict(PyObject *dict) {
    PyObject *key;
    PyObject *value;
    Py_ssize_t pos = 0;

    while (PyDict_Next(dict, &pos, &key, &value)) {
        if (!PyUnicode_Check(key)) {
            PyErr_Format(PyExc_TypeError, "ERROR: Failed to dump key\n");
            return 0;
        }

        if (!PyUnicode_Check(value) && !PyLong_Check(value)) {
            PyErr_Format(PyExc_TypeError, "ERROR: Failed to dump value\n");
            return 0;
        }
    }
    return 1;
}

PyObject *cjson_dumps(PyObject *self, PyObject *args) {
    PyObject *dict = NULL;
    if (!PyArg_ParseTuple(args, "O", &dict)) {
        PyErr_Format(PyExc_TypeError, "ERROR: Expected dict as argument\n");
        return NULL;
    }

    if (!PyDict_CheckExact(dict)) {
        PyErr_Format(PyExc_TypeError, "ERROR: Expected dict as argument\n");
        return NULL;
    }

    if (!check_dict(dict)) {
        return NULL;
    }

    PyObject *repr = PyObject_Repr(dict);
    char *str = PyBytes_AS_STRING(PyUnicode_AsEncodedString(repr, "utf-8", "~E~"));

    char *found_char;
    while ((found_char = strchr(str, '\'')) != NULL) {
        *found_char = '\"';
    }

    return Py_BuildValue("s", str);
}

static PyMethodDef methods[] = {
    {"loads", cjson_loads, METH_VARARGS, NULL},
    {"dumps", cjson_dumps, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef module_cjson = {
    PyModuleDef_HEAD_INIT,
    "cjson",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_cjson() {
    return PyModule_Create(&module_cjson);
}
