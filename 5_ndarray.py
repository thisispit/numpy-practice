import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print the total no of element of the array
print(arr.size)

# Print the shape of the array ie:(2,5)
print(arr.shape)

# pirnt the no of dimesion ie 2,3
print(arr.ndim)

# prints the data type of the element of the array
print(arr.dtype)

# returns the size of one array element in bytes
print(arr.itemsize)

# return the total memory consumed bt the array in bytes
print(arr.nbytes)

# transpose of the array
print(arr.T)

# iterate over all the element of the array using loop
print(f"Flat itetator: ")
for item in arr.flat:
    print(item,end=" ")