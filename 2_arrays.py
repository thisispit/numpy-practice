import random
import numpy as np

# zeros matrices
zero = np.zeros((4,4))
print(zero)

# ones matrices
ones = np.ones((4,4))
print(f"\n{ones}")

# fixed matrices of 7
f= np.full((4,4),7)
print(f"\n{f}")

# random array
random = np.random.random((3,3))
print(f"\n{random}")

# sequence of array
seq = np.arange(1, 10, 0.5)
print(f"\n{seq}")
