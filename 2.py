def print_value(dictionary, key):
    if key in dictionary:
        print(dictionary[key])
    else:
        print("Key not found")

sample_dict = {'a': 1, 'b': 2, 'c': 3}
print_value(sample_dict, 'b')
print_value(sample_dict, 'd')
