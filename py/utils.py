def params_to_obj(list_params):
    obj = {}
    for param in list_params:
        name, value = tuple(param.split('='))
        obj[name] = value.replace("_", "")

    return obj
