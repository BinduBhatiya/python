# python built-in math function.

# min(), max() :
p = min(10,20,30)
q = max(10,20,30)

print('minimum is: ',p)         # minimum is:  10
print('maximum is: ',q)         # maximum is:  30

# abs() :
# it return absolute value.
p = abs(-7.25)
print(p)                        # 7.25

# pow() :
# The pow(x, y) function returns the value of x to the power of y (xy).

a = pow(4,3)
print('power of 4 is: ',a)      # power of 4 is: 64  


# sqrt() :
# it return square root of given value.

import math
a = math.sqrt(64)
print('square root of 64 is: ',a)       # square root of 64 is:  8.0


# floor() and ceil() :
# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


# pi() :
# The math.pi constant, returns the value of PI (3.14...)

import math
x = math.pi
print(x)            # 3.14