import numpy as np;

arr = np.array([1, 2, 3, 4, 5])
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

arr = np.arange(1, 11)
print(f"The numpy array using arange: {arr}");
print("\t\t", '-' * 15)

arr = np.zeros(2)
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

# Create 2x3 array of zeros 
arr = np.zeros((2, 3))
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

arr = np.ones(2)
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

# creates 2x2 array of ones
arr = np.ones((2, 2))
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

arr = np.full(2, 2)
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

# creates 2x2 array using 11 as constant
arr = np.full((2, 2), 11)
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

arr = np.eye(4, 3)
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

# create 4x4 identity array
arr = np.eye(4)
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

arr = np.eye(2, 3)
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

arr = np.random.random(3)
print(f"The numpy array is: {arr}")
print("\t\t", '-' * 15)

# creates 3x3 array using random values
arr = np.random.random((3, 3))
print(f"The numpy array is: {arr}")