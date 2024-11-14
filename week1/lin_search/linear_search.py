def linear_search(val, arr_to_search):
    for i, obj in enumerate(arr_to_search):
        if val == obj:
            return i
    return None

def linear_search_global(val, arr_to_search):
    indexes = []
    for i, obj in enumerate(arr_to_search):
        if val == obj:
            indexes.append(i)
    if len(indexes) == 0:
        return None
    else:
        return indexes