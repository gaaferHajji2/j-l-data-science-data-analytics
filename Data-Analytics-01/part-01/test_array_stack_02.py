import numpy as np

# Create 1-D array
arr1 = np.arange(4, 7)
print(f"The arr1 is: {arr1}")

arr2 = 2 * arr1
print(f"The arr2 is: {arr2}")

# create column stack
arr_col_stack = np.column_stack((arr1, arr2))
print(f"The arr col stack: {arr_col_stack}")

# create row stack
arr_row_stack = np.vstack((arr1, arr2))
print(f"The arr row stack is: {arr_row_stack}")