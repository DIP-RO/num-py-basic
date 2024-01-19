""""
vstack()   =  this function stacks arrays vertically
dstack()  = this function stacks arrays depth-wise along the third axis
hstack()  = this function stacks arrays horizontally
column_stack() = this function stacks one-dimensional arrays as columns to create a two-dimensionally array
row_stack() = this function stacks array vertically
concatenate() = this function  concatenates a list or a tuple of arrays
"""
import numpy as np

"""""horizontal"""
a = np.array([[7, 2, 2],
              [2, 2, 9],
              [7, 9, 7]])

b = 2 * a

c = np.hstack((a, b))
print(c)

# column_stack()
print("Column_stack:")

d = np.column_stack((a, b))
print(d)

# concatenate()

print("concatenate:")
e = np.concatenate((a, b), axis=1)
print(e)

''''vertical stacking'''
print("vstack:")
f = np.vstack((a, b))
print(f)

print("concatenate:")
g = np.concatenate((a, b), axis=0)
print(g)

print("row_stack:")
h = np.row_stack((a, b))
print(h)

#depth_stack()  for 3rd axis
print("dstack:")
u = np.dstack((a,b))
print(u)