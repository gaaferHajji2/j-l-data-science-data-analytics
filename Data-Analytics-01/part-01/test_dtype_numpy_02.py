import numpy as np

arr = np.arange(1, 11)
print(type(arr))
print(arr.dtype)
print(arr.shape)

arr = np.random.random((3, 3))
print(f"The array is: {arr}")
# Access item in 0 0
print(arr[0,0])
# Access item in 1 2
print(arr[1, 2])

arr = np.array([[2, 1, 7], [3, 5, 8]])
print(f"The array is: {arr}")
# Access item in 0 0
print(arr[0,0])
# Access item in 1 2
print(arr[1, 2])
