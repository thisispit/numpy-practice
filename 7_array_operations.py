import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [4 10 18]
print(a / b)   # [0.25 0.4  0.5 ]

# scaler operations 
print(a+15)
print(a*10)

# mathematical functions
print("SQRT of array a: ",np.sqrt(a))
print("Exponential of array a: ",np.exp(a))
print("Log of array a: ",np.log(a))
print("Sin of array a: ",np.sin(a))

# Aggregation Functions
print(a.sum())
print(a.mean())
print(a.max())
print(a.min())
print(a.std())
print(a.var())

# Matrix Operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)   # Matrix multiplication 
print(np.transpose(A))  # Transpose
print(np.linalg.inv(A)) # Inverse 
