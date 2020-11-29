
none_var = None

# -- int --

int_none = int()
int_var = 5
int_var1 = 3
real_var = 3.13

sum_var = 5 + 3.13
sum_varr = int_var + real_var
substr_var = int_var - int_var1
mult_var = int_var * int_var1
div_var = int_var / int_var1
div_mod = int_var % int_var1

# -- str --

str_none = str()
str_var = 'test'
str_var1 = 'my'
str_empty = ''

sum_str = str_var1 + ' ' + str_var
mult_str = str_var * int_var1

# -- bool --

bool_true = True
bool_false = False
bool_none = bool()

# -- eval() --

eval_val = bool(bool_none)



print(eval_val)
print(int_none)
print(bool_none)
print(str_none)

print(str_var)
print(str_empty)
print(sum_str)
print(mult_str)


# print(int_var)
# print(none_var)
# print(real_var)
# print(sum_var)
# print(substr_var)
# print(mult_var)
# print(div_var)
# print(div_mod)
