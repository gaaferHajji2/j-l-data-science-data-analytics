import numpy as np

arr = np.arange(1, 10).reshape(3, 3)
print(f"arr is: {arr}\ntype is: {arr.dtype}")
arr = arr.astype(np.float64)
print(f"arr is: {arr}\ntype is: {arr.dtype}")
l1 = arr.tolist()
print(f"l1 is: {l1}\nl1 type:{type(l1)}")