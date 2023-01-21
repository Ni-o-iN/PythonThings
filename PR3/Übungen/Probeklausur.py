a = 8
if a > 0:
    print('A')
print('B')


def min(x,y):
    if x < y:
        print(x)
    else:
        print(y)
min(2,3)


a = [2, 3, 5, 7]
a[-1] = 9
a[0] = 6
print(a)


a = [1,2,3,4,5,6,7,8,9]
b = filter(lambda x: x % 2 == 0, a)


print({1, 2, 4, 8, 16}.issubset({1, 4, 16, 64, 256})) # false
print({1, 2, 4, 8, 16}.difference({1, 4, 16, 64, 256})) # {2,8}
print({1, 2, 4, 8, 16}.symmetric_difference({1, 4, 16, 64, 256})) # {2,8,64,256}

