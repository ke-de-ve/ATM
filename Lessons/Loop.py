list_var = ['first', 'second', 'third']

# for <var> in <list>
# 1. var = list[0]
# print(var)
for element in list_var:
    print(element)
    # if element == 'second':
    #     print('few more actions!')

print('For finished its work')

list_none = []
for i in list_none:
    print('nothing')

str_var = 'best test ever'
for char in str_var:
    print(char)

dict_var = {'first': 1, 'second': 2, 'third': 3}
for key, value in dict_var.items():   # key, value = 'first', 1
    print('key: {}'.format(key))
    print('value: {}'.format(value))

var1 = int()
var2 = int()

var1 = var2 = 4

print('var1 = {}'.format(var1))
print('var2 = {}'.format(var2))

var1, var2 = 4, 8
print('var1 = {}'.format(var1))
print('var2 = {}'.format(var2))

var1 = 3
var2 = 9
print('var1 = {}'.format(var1))
print('var2 = {}'.format(var2))


for key in dict_var.keys():
    print(key)

dict_var['fourth'] = 4
for value in dict_var.values():
    if value == 4:
        print('Value = {}. Victory!'.format(value))
    else:
        print('not yet, value = {}'.format(value))
