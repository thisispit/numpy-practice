import numpy as np
import time

# creating arrays

array_1d = np.array([1,2,3,4,5])
print(f"1d array: {array_1d}")

array_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(f"2d array: {array_2d}")

# Multiplying each element of an 2d array
print(f"2D Array multipication: {array_2d*2}") 

# Comparing Python list VS NumPy array Operation Time
start = time.time()
py_list=[i*5 for i in range (100000)]
print(f"Oeration Time for Python list: {time.time() - start}")

start =time.time()
py_array=np.arange(100000)*5
print(f"Operation Time for numPy array: {time.time() - start}")