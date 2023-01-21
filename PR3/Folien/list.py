a = [1,2,3]
b = [[1,2],
     [3,4]]


print(a)
print(b)


for row in b:
     for item in row:
          print(item, end=" ")
     print()


x = 4
a[1:2] = [x, 5]
print(a)
print(4 in a)


for num in range(2,10):
     if num % 2 == 0:
          print("gerade")
          continue
     print("ungerade")


t = [1,2,3,4,5,6,7,8]
gerade = list(filter(lambda i: i % 2 == 0, t))
print(gerade)


def rechnen(n):
     return rechnen(n-1)+rechnen(n-2) if n > 2 else 1
print(rechnen(4))