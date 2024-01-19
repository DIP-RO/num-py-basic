"""
Module Name: array attribute
A brief description of your module.
Provide more details about what the module does and any relevant information.
"""

import numpy as np


a = np.array([1, 2, 3])  # 1-dimensional /vector
print( a)
print(type(a))
print(a.shape)
print(a.ndim)

b = np.array([[1, 2, 3], [4, 5, 6]])  # 2-dimensional
print(b)
print(type(b))
print(b.shape)
print(b.ndim)
b = np.array([[[1, 2, 3],
               [4, 5, 6],
               [4, 5, 6]]])
print(b)
print(b.dtype)
print(b.size)
print(b.nbytes)