import numpy as np

a = np.array([[1,3,5],[2,4,6]])
print("a:\n",a)
print("a Summe:\n",a.sum())
b = np.array([[3,1,5],[6,2,4]], float)
print("b:\n",b)
c = np.zeros((2,3))
print("c:\n",c)
print("c shape:\n",c.shape)
d = np.diag([1,2,3])
print("d:\n",d)
e = np.random.random((2,3))
print("e:\n",e)
np.savetxt("array.txt", e)

x_array = np.array([0,1,2])
y_array = np.array([3])
print(x_array + y_array)