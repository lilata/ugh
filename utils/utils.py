import json
def updated_dict(*args):
    if len(args) == 0:
        return {}
    if len(args) == 1:
        if isinstance(args[0], dict) is False:
            return {}
        else:
            return args[0]
    start = args[0] if isinstance(args[0], dict) is True else {}
    for d in args[1:]:
        if not isinstance(d, dict):
            continue
        start.update(d)
    return start
def load_body_as_json(request):
    try:
        data = json.loads(str(request.body, encoding='utf-8'))
    except json.JSONDecodeError:
        data = {}
    return data