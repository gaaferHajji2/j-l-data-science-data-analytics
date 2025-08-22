import numpy as np

arr = np.arange(1, 10).reshape(3, 3)
print(f"The arr is: {arr}")
# Perform horizontal splitting
arr2 = np.hsplit(arr, 3)
print(f"the arr after hsplit is: {arr2}")

arr3 = np.vsplit(arr, 3)
print(f"The arr after vsplit is: {arr3}")