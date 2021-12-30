"""
Array of 1 dimension, shape is (3,) since there is only 1 dimension
Another way to think of it would be a line (length)
test_array = np.array([1, 2, 3])
print(test_array)
print(test_array.ndim)
print(test_array.shape)
"""

"""
Array of 2 dimensions, shape is (3, 3)
Another way to think of it would be a square (width and length)
test_array = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print(test_array)
print(test_array.ndim)
print(test_array.shape)
"""

"""
Array of 3 dimensions, shape is (3, 3, 3)
For a shape, it would be a cube (width, length, and depth)
test_array = np.array([[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]],
                       [[10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18]],
                       [[19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27]]])
print(test_array)
print(test_array.ndim)
print(test_array.shape)
"""

"""
Array of 4 dimensions, shape is (3, 3, 3, 3)
For a shape, it would be a tesseract (width, length, and depth, time)
test_array = np.array([[[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]],
                       [[10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18]],
                       [[19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27]]],
                       [[[28, 29, 30],
                        [31, 32, 33],
                        [34, 35, 36]],
                       [[37, 38, 39],
                        [40, 41, 42],
                        [43, 44, 45]],
                       [[46, 47, 48],
                        [49, 50, 51],
                        [52, 53, 54]]],
                       [[[55, 56, 57],
                        [58, 59, 60],
                        [61, 62, 63]],
                       [[64, 65, 66],
                        [67, 68, 69],
                        [70, 71, 72]],
                       [[73, 74, 75],
                        [76, 77, 78],
                        [79, 80, 81]]]])
print(test_array)
print(test_array.ndim)
print(test_array.shape)
"""