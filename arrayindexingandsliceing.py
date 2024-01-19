import numpy as np

# indexing
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1[0])
print(arr1[4])

arr2 = np.random.randint(1, 10, size=(3, 3))
print(arr2)
print(arr2[1][0])
arr3 = np.random.randint(1, 10, size=(3, 3, 3))
print(arr3)
print(arr3[2][2][1])

# slicing
print(arr1[0:3])
print(arr1[3:])
print(arr2[0:2, 0:2])
