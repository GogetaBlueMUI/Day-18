def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)
