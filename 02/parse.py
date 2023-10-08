import json


def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback=None):
    try:
        json_doc = json.loads(json_str)
    except TypeError:
        print('json_str should be str')
        return

    if not isinstance(required_fields, list) or not isinstance(keywords, list) or not callable(keyword_callback):
        print('put required_fields and keywords as list and keyword_callback as function')
        return

    for i, keyword in enumerate(keywords):
        keywords[i] = keywords[i].lower()

    fields = [field for field in required_fields if field in json_doc]

    for field in fields:
        for keyword in keywords:
            if keyword in (json_doc[field].lower()).split():
                keyword_callback(field, keyword)


def callback():
    pass
