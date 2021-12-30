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