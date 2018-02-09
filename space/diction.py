convertible_int = ['float', 'float64', 'int64']

def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result



def convert_all_possible_float_to_int(obj):
    for key, value in obj.items():
        value_type = type(value).__name__
        if value_type in convertible_int:
            obj[key] = int(value)
        elif value_type == 'dict':
            obj[key] = convert_all_possible_float_to_int(value)
        elif value_type == 'list':
            obj[key] = convert_to_int_list(value)

    return obj

def convert_to_int_list(ls):
    new_ls = list()
    for val in ls:
        type_val = type(val).__name__
        if type_val in convertible_int:
            new_ls.append(int(val))
        elif type_val == 'dict':
            new_ls.append(convert_all_possible_float_to_int(val))
        else:
            new_ls.append(val)
    return new_ls
