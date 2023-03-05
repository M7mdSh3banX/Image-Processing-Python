import numpy as np

# Version of numpy library
print(np.__version__)

# Create a NumPy ndarray Object - 1-D Arrays
oneD_arr = np.array([1, 2, 3, 4, 5])
print("One Dimensional Array: ", oneD_arr)

# the type of the object passed to it
print("Type of Array: ", type(oneD_arr))

# 0-D Arrays
zeroD_arr = np.array(42)
print("Zero Dimensional Array: ", zeroD_arr)

# 2-D Arrays
twoD_arr = np.array([[1, 2, 3], [3, 4, 5]])
print("Two Dimensional Array: ", twoD_arr)

# 3-D Arrays
threeD_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("Three Dimensional Array: ", threeD_arr)

# Check Number of Dimensions
print('number of dimensions :', zeroD_arr.ndim)
print('number of dimensions :', oneD_arr.ndim)
print('number of dimensions :', twoD_arr.ndim)
print('number of dimensions :', threeD_arr.ndim)

# Higher Dimensional Arrays
highD_arr = np.array([1, 2, 3, 4], ndmin=5)

print("Five Dimensional Array: ", highD_arr)
print('number of dimensions :', highD_arr.ndim)

# Access Array Elements
print(oneD_arr[0])
print('2nd element on 1st row:', twoD_arr[0, 1])
print(threeD_arr[0, 1, 2])

# Negative Indexing
print('Last element from 2nd dim: ', twoD_arr[1, -1])
