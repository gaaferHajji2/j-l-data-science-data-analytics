import numpy as np

arr = np.arange(1, 5).reshape(2, 2)
arr_no_copy = arr
arr_copy = arr.copy()
arr_view = arr.view()
print(f"the id of array: {id(arr)}")
print(f"the id of arr no copy: {id(arr_no_copy)}")
print(f"the id of arr copy: {id(arr_copy)}")
print(f"the id of arr view: {id(arr_view)}")

arr_view[0][0] = 9
# Same result
print(f"original arr: {arr}")
print(f"arr view: {arr_view}")