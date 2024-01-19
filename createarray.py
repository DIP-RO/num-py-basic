"""
Module Name: array attribute
A brief description of your module.
Provide more details about what the module does and any relevant information.
"""

import numpy as np

array1 = np.array([1, 2, 3], dtype='int')
print(array1)

# zeros
zeros = np.zeros((2, 2), dtype='float')
print(zeros)
# ones
ones = np.ones((2, 2), dtype='float')
print(ones)

# full

full = np.full((2, 3), 5)
print(full)
# identity
identity = np.identity(3, dtype='int')
print(identity)

# eye
eye = np.eye(3, 3, 1)
print(eye)

# arrange
arrange = np.arange(1, 10, 2)  # parameter(start,end,space)
print(arrange)
# lines space
linspacess = np.linspace(1, 10, 10)  # parameter(start,end,no of elements)
print(linspacess)
print(linspacess.size)

# empty
empty = np.empty((1, 5))  # parameter(shape , dtype , order='c')
print(empty)
for i in range(5):
    empty[:, i] = i
print(empty)
