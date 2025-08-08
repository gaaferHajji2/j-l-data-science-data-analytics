import numpy as np

print(np.float32(21))
print(np.int8(21.0)) # --> 21
print(np.bool(21))
print(np.bool(0))
print(np.bool(21.0))
print(np.float32(True))
print(np.float32(False))

print(np.arange(1, 11, dtype=np.float32))

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"The Array data type is: {arr.dtype}")
print(f"The Array data type for item size is: {arr.dtype.itemsize}")

arr1 = np.arange(1, 11, dtype='f')
print(f"The array with dtype f is: {arr1}")

arr2 = np.arange(1, 11, dtype='D')
print(f"The array with dtype D is: {arr2}")