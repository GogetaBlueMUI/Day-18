my_dict = {'a': 1, 'b': 2}
try:
    print(my_dict['c'])
except KeyError:
    print("Custom error: Key not found")
