# comments
test_str = 'test string'
test_int = 5
hello = 'Hello {}'

# test variables
divider = ' '
str1 = 'test1'
str2 = 'test2'
str3 = 'test3'
test_list = [str1, str2, str3]

test_join = ' '.join(['check', 'my', 'result'])

print('Hello World!')
print(test_str*test_int)
print((test_str+' ')*test_int)
print(hello.format('Jenya'))
print(test_join)
print(divider.join(test_list))

print(even(test_int))
