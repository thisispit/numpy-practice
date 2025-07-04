
import numpy as np

arr= np.array([10,20,30,40])

# return first element
print(arr[0])

# reverse idexing
print(arr[-1])

# slice from index 1 to 3
print(arr[1:4])

# slice from start to 3
print(arr[:3])

# every second element
print(arr[1::2])


## 2D arrays
arr_2d=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])

# return entire second row
print(arr_2d[1])

# entire first column
print(arr_2d[:,0])

# row 0, column 1
print(arr_2d[0,1])

# bottom right sub matrix
print(arr_2d[1:,2:])


# negative indexing
print(arr_2d[-1,-1])

# boolean indexing
print(arr_2d[arr_2d > 10])