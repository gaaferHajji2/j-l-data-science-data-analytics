import numpy as np

arr = np.arange(12)

print(f"Array before reshape: {arr}")

# the reshape must equal to size array: ex: 12
print(f"Array with reshape: {arr.reshape(4, 3)}")

arr = np.arange(12).reshape(4, 3)
print(f"Array before flatten: {arr}")

print(f"Array after flatten: {arr.flatten()}")

arr2 = arr.ravel()
print(f"The Array after ravel: {arr2}")

print(f"The transpose of arr is: {arr.transpose()}")

# ValueError: cannot resize this array: it does not own its data
# We must first create copy of the array
arr3  = arr.copy()
arr3.resize(2, 3)
print(f"The Array after resize: {arr3}")