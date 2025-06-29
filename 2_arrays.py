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

## Random Class

# random.random(size) lies from 0 to 1)
r = np.random.random((4,4))
print(r)

# random.choice(array, size, replace)
a = np.random.choice(('Apple','Ball','Cat'),3)
print(a)

# randint(low, high, size)
b = np.random.randint(1,10,5)
print(b)

# random.normal(0, 1, 4)
c = np.random.normal(1,5,5)
print(c)