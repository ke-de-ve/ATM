list_null = list()
list_null1 = []

print(list_null)

# _index____0__1__2
list_int = [0, 1, 2]

print(list_int)
print(  list_int[1]  )
print(  list_int[2]  )

list_bool = [False, True, True]

print(list_bool)
print(list_bool[2])

list_str = ['str0', 'test', 'null']

print(list_str)
print(list_str[1])

list_mixed = []

print(list_mixed)
# print(list_mixed[0])


list_mixed.append('First')
print(list_mixed)
print(list_mixed[0])

list_mixed.append('Second')
print(list_mixed)
print(list_mixed[1])

list_mixed[0] = 5
print(list_mixed)
print(list_mixed[0])

list_len = len(list_mixed)
print(list_len)

str_var = 'test'
str_len = len(str_var)
print(str_len)

print(str_var[1])

# ----- Dict ------

dict_null = dict()
dict_null1 = {}

print(dict_null)
print(bool(dict_null))

dict_var = {"string1": "test1", 'int2': 7}

print(dict_var)
print(dict_var['string1'])

dict_var['string1'] = 'not a string'
print(dict_var)

# create a new key value pair
dict_var['new key'] = 'new value'
print(dict_var)

# override new key value
dict_var['new key'] = 'override new value'
print(dict_var)

print(dict_var.get('unknown'))

dict_len = len(dict_var)
print(dict_len)

dict_keys = dict_var.keys()
print(dict_keys)
dict_values = dict_var.values()
print(dict_values)
