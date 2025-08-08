import numpy as np

arr = np.arange(1, 10).reshape(3, 3)
print(f"The array is: {arr}")

arr2 = arr * 2;
print(f"The new array is: {arr2}")

arr3 = np.hstack((arr, arr2))
print(f"The hstack array is: {arr3}")

arr4 = np.vstack((arr, arr2))
print(f"The vstack array is: {arr4}")

arr5 = np.concatenate((arr, arr2), axis=1)
print(f"The Array of concatenate, with axis 1 : {arr5}")

arr6 = np.concatenate((arr, arr2), axis=0)
print(f"The Array of concatenate, with axis 1 : {arr6}")
