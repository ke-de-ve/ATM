# list +
list_a = list(range(8))

print(list_a)

# [0, 1, 2, 3, 4, 5, 6, 7]
# -8 -7 -6 -5 -4 -3 -2 -1

print(list_a[-1])
print(list_a[len(list_a)-1])

print(list_a[-3])

i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print('loop is out')

print('Bingo!')