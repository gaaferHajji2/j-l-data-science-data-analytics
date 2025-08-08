import numpy as np

print(np.dtype('f')) # --> float32
print(np.dtype('f8')) # --> float64
print(np.dtype('d')) # --> float64
print(np.dtype(float)) # --> float64

var2=np.array([1,2,3],dtype='float64')
print(var2.dtype.char) # --> d
print(var2.dtype.type) # --> <class 'numpy.float64'>