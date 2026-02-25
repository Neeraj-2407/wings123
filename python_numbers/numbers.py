x = 10    # int
y = 3.8  # float
z = 2j   # complex
print(type(x))
print(type(y))
print(type(z))

x = 11    # int
y = 5.6  # float
z = 5j  # complex

a = complex(x)

b = int(y)

c = float(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random_number
import random

print(random.randrange(1, 18))