import numpy as np

arr = np.arange(21, 41, 2)
arr2 = arr[arr>30]
print(f"arr: {arr}")
print(f"after boolean slicing: {arr2}")

# Fancy Indexing
arr = np.arange(1, 21).reshape(5, 4)
indecies = [1, 2]
print(f"The arr after indexing: {arr[indecies]}")

# Selecting sub array
row = np.array([1, 2])
col = np.array([2, 3])
print(f"array after indexing: {arr[row, col]}")