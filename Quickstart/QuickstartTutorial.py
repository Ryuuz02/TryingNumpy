import numpy as np
import matplotlib as plt

"""
Creates a 1 axis array with the numbers 1-15
test_array = np.arange(15)
"""
"""
Does the same, but reforms it into 3 rows each with a length of 5
test_array = np.arange(15).reshape(3, 5)

Prints out the array
print(test_array)
Prints out the shape (is 3x5 as we specified above)
print(test_array.shape)
ndim is the number of dimensions, basically how many axes it has
print(test_array.ndim)
dtype is the data type stored in the array, in this case int32
print(test_array.dtype.name)
Prints out the data size of the array in bytes
print(test_array.itemsize)
Prints out the size of the array (15 in this case)
print(test_array.size)
Prints out its class type (numpy.ndarray for this)
print(type(test_array))
"""

"""
You can specify the data type of the array when it is made
test_array = np.array([1, 2, 3], dtype=complex)
print(test_array)
print(test_array.dtype.name)
"""

"""
You can make an array of zeroes using .zeros
test_array = np.zeros((3, 5, 4))
print(test_array)
"""

"""
Similarly, you can fill it with ones using ones
test_array = np.ones((2, 2, 3), dtype=np.int16)
print(test_array)
"""

"""
You can also make one filled with random values using .empty Their value can vary greatly from incredibly small to 
massive as it is entirely dependent on the computer's memory state
test_array = np.empty((3, 3, 3))
print(test_array)
"""

"""
If you want to make an incremental series of numbers, use .arange. It functions very similar to the python range 
function, but uses an array rather than a list (Note that arange is not a misspelt version of arrange, but an 
a(rray) range, hence the name
test_array = np.arange(1, 10, 2)
print(test_array)
"""

"""
You can also use arange with decimals, but the accuracy of the length is unreliable due to how floats are handled in 
coding
test_array = np.arange(0.2, 2, 0.4)
print(test_array)
"""

"""
If you try to print an array that is incredibly large, it will just cut out the center in display and leave the corners
test_array = np.arange(10000)
print(test_array)

test_array = np.arange(10000).reshape(100, 100)
print(test_array)
"""

"""
Math equations are done by element

test_array1 = np.array([20, 25, 30, 35])
test_array2 = np.arange(4)

You can save the results to the variable and the print it to keep the results
test_array1 -= test_array2
print(test_array1)
test_array2 = test_array2 ** 2
print(test_array2)

Or you can print it out by itself, this will not change the array you are using, just display it
print(10*np.sin(test_array1))
print(test_array1 < 30)
"""

"""
Most operators work as expected, however if you want o find the matrix product of two arrays, you can use @
test_array1 = np.array([[1, 2],
                       [3, 4]])
test_array2 = np.array([[4, 3],
                       [2, 1]])
print(test_array1 @ test_array2)
"""

"""
Important to note data types when using operators between arrays, the data type must be valid as they are not 
automatically converted
"""

"""
When you use operators between two valid types, the resulting array will be the type that is more precise
"""

"""
There are multiple functions of arrays that you can call to analyze the information in them, some examples below
test_array = np.arange(4).reshape(2, 2)
print(test_array.sum())
print(test_array.max())
print(test_array.min())
"""

"""
You can also specify the axis to use when calling those functions
test_array = np.arange(12).reshape(2, 2, 3)
print(test_array)
print(test_array.sum(axis=0))
print(test_array.sum(axis=1))
print(test_array.sum(axis=2))
"""

"""
You can also use normal mathematical functions with numpy array
test_array = np.arange(5)
print(np.exp(test_array))
test_array2 = np.arange(5, 10)
print(np.add(test_array, test_array2))
print(np.sqrt(test_array))
"""

"""
Indexing and slicing with arrays
For each axis in the array that you are looking through, the bracket index [] has one more value
for example, a 1d array would just be [value], a 2d array would be [value, value], 3d would be [value, value, value]
These values can be one of two things: either an int, such as with a 3d array using [1, 1, 1]
                                       Or it can be a range, which would mean all those values within that range
                                       For example, with a 3d array you could do [0:5, 1, :]
test_array = np.arange(10).reshape(2, 5)
print(test_array)
print(test_array[(0, 1)])
print(test_array[:, 1])
test_array = np.arange(27).reshape(3, 3, 3)
print(test_array)
print(test_array[0, 0, 0])
print(test_array[:, 1, 0])
print(test_array[:, 1:2, :])
"""

"""
For iterating through an array in a loop, you can have it go through the first index repetitively
test_array = np.arange(10).reshape(5, 2)
for row in test_array:
    print(row)
"""

"""
There are multiple ways to reshape an array in numpy

test_array = np.arange(10).reshape(2, 5)
print(test_array)

    Reshape changes the shape of the array into the specified values
print(test_array.reshape(5, 2))

    array.ravel() unravels the array into one long axis
print(test_array.ravel())

    array.T transposes it, meaning that it basically rotates the array 90 degrees clockwise
print(test_array.T)

    Whereas .reshape returns the reshaped array, you can use .resize to change the variable itself without using array =
test_array.resize(5, 2)
print(test_array)

    You can use a -1 in reshape to have it automatically calculated to what it should be
test_array = np.arange(27)
print(test_array.reshape(3, 3, -1))
"""


"""
You can stack arrays on top of eachother using vstack (vertical stack) and hstack (horizontal stack)
test_array1 = np.arange(6).reshape(3, 2)
test_array2 = np.arange(6, 12).reshape(3, 2)
print(np.vstack((test_array1, test_array2)))
print(np.hstack((test_array1, test_array2)))
"""

"""
You can split arrays both horizontally and vertically, with hsplit and vsplit respectively
The easiest way to think of it is that the horizontal and vertical split, cut it the opposite way of their name. So an 
hsplit would make vertical cuts in an array, and a vsplit would make horizontal cuts
test_array = np.arange(24).reshape(4, 6)
print(test_array)

    You can use a single value to specify how many arrays you want it to be split into
print(np.hsplit(test_array, 3))

    Or a tuple in order to specify at what columns/rows it should split at
print(np.hsplit(test_array, (3, 4)))

    Same process for vsplit
print(np.vsplit(test_array, 2))
print(np.vsplit(test_array, (1, 3)))
"""