def print_test(var1):
    print('lets test begin')
    res = var1 + 2
    print(res)
    print('this is our TEST!')

def print_default_value(var1=9):
    print('lets test begin')
    res = var1 + 2
    print(res)
    print('this is our TEST!')

def print_multiple_value(var1, var2=6):
    print('lets test begin')
    res = var1 + var2
    print(res)
    print('this is our TEST!')

def print_multiple_value_order(var1, var2='default'):
    print('lets test begin')
    print(var1+1)
    print(var2+' value!')
    print('this is our TEST!')

def calc_val(var1, var2=2):
    summ = var1 + var2
    print(var1)
    print(var2)
    print_ok = print(summ)

    return summ

# def main():
#     print('this is main!')

print('this is script')

print_test(5)
print_default_value(22)
print_multiple_value(34, 8)
print_multiple_value_order(3)
result = calc_val(1)

print('result = {}'.format(result))

var1, var2, var3 = 1, 2, 3

msg = 'long long long log file with a bunch of extra variables here. It should not be longer than 80 symbols :{}, {}, {}'
print(msg.format(var1, var2, var3))
