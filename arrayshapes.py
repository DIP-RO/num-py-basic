import numpy as np

# reshape()


a = np.array([[1, 2, 3],
              [2, 3, 4]])
print(a)
print(a.shape)
b_aReshaped = np.reshape(a, (3, 2))
print(b_aReshaped)

# resize()

a_resized = np.resize(a, (4, 3))
print(a_resized)

# ravel()

b = np.random.randint(1, 10, size=(3, 3))  # return a view of the array   and also chnage the main array
print(b)

b_raveled = np.ravel(b)
print(b_raveled)
print(b_raveled.shape)

# flatten()

b_flattened = b.flatten()  # return a copy of the array  and always allocate a new memory
print(b_flattened)

# defining an array shape
print("array:")
print(b)
print(b.shape)
