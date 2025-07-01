import numpy as np 

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