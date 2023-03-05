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

# Slicing arrays: [start:end] or [start:end:step]
sliced_arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slice elements from index 1 to index 5
print(sliced_arr[1:5])

# Slice elements from index 4 to the end of the array
print(sliced_arr[4:])

# Slice elements from the beginning to index 4
print(sliced_arr[:4])

# Negative Slicing - slice from the index 3 from the end to index 1 from the end
print(sliced_arr[-3:-1])

# Slice with step
print(sliced_arr[1:5:2])

# Return every other element from the array by 2 steps
print(sliced_arr[::2])

# From both elements, return index 2
my_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(my_arr[0:2, 2])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print(my_arr[0:2, 1:4])

# Checking the Data Type of Array
print(my_arr.dtype)

# Creating Arrays With a Defined Data Type
defined_arr = np.array([1, 2, 3, 4], dtype='S')
print(defined_arr)
print(defined_arr.dtype)

# Converting Data Type on Existing Arrays
float_arr = np.array([1.1, 2.1, 3.1])
int_arr = float_arr.astype(int)

print(int_arr)
print(int_arr.dtype)

""" Data Types in NumPy
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

""" astype function's arguments
int
bool
complex
float
object
str
"""

# Copy
original_arr = np.array([1, 2, 3, 4, 5])
copy_arr = original_arr.copy()
original_arr[0] = 42

print(original_arr)
print(copy_arr)

# View
original_arr = np.array([1, 2, 3, 4, 5])
view_arr = original_arr.view()
original_arr[0] = 42

print(original_arr)
print(view_arr)

# Get the Shape of an Array
print(my_arr.shape)
print(original_arr.shape)
print(highD_arr.shape)

# Reshape From 1-D to 2-D
old_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = old_arr.reshape(4, 3)
print(new_arr)

# Flattening array means converting a multidimensional array into a 1D array.
ordinary_arr = np.array([[1, 2, 3], [4, 5, 6]])
flat_arr = ordinary_arr.reshape(-1)
print(flat_arr)

# Iterating on Each Scalar Element using nditer()
iterating_arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in np.nditer(iterating_arr):
    print(i)

# Enumerated Iteration Using ndenumerate()
for idx, x in np.ndenumerate(iterating_arr):
    print(idx, x)

# Joining NumPy Arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
joined_array = np.concatenate((array1, array2))
print(joined_array)

# Join two 2-D arrays along rows (axis=1)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
joined_array2 = np.concatenate((arr1, arr2), axis=1)
print(joined_array2)

# Split array
split_array = np.array_split(old_arr, 3)
print(split_array)

# Searching Arrays
search_arr = np.array([1, 2, 3, 4, 5, 4, 4])
print(np.where(search_arr == 4))

# Search Sorted performs a binary search in the array
# returns the index where the specified value would be inserted to maintain the search order.
bsearch_array = np.array([6, 7, 8, 9])
print(np.searchsorted(bsearch_array, 7))

# Sorting Arrays
unsorted_arr = np.array([3, 2, 0, 1])
print(np.sort(unsorted_arr))

# Filtering Arrays
unfiltered_arr = np.array([41, 42, 43, 44])
filtered_arr = unfiltered_arr[[True, False, True, False]]
print(filtered_arr)

# Creating Filter Directly From Array
filtered_arr = unfiltered_arr[unfiltered_arr > 42]
print(filtered_arr)