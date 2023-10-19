class CustomMeta(type):
    def __new__(mcs, name, bases, classdict, **kwargs):
        custom_dict = {}
        for name_attr, value in classdict.items():
            if not name_attr.startswith('__') and not name_attr.endswith('__'):
                custom_dict[f"custom_{name_attr}"] = value
            else:
                custom_dict[name_attr] = value

        def set_attr(cls, key, value):
            if not key.startswith('custom') and not key.startswith('__') and not key.endswith('__'):
                cls.__dict__[f'custom_{key}'] = value

        custom_dict['__setattr__'] = set_attr

        cls = super().__new__(mcs, name, bases, custom_dict)
        return cls

    def __setattr__(cls, key, value):
        if not key.startswith('custom') and not key.startswith('__') and not key.endswith('__'):
            key = f'custom_{key}'
        super(CustomMeta, cls).__setattr__(key, value)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
