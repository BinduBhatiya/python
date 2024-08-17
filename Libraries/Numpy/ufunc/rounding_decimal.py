# Rounding Decimal :
'''
There are primarily five ways of rounding off decimals in NumPy:
    1. truncation
    2. fix
    3. rounding
    4. floor
    5. ceil
'''
# Truncation :
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

import numpy as np
arr = np.trunc([-3.1666, 3.6667])
print("truncation: ",arr)       # truncation:  [-3.  3.]
arr1 = np.fix([-3.1666, 3.6667])
print("truncation1: ",arr1)       # truncation1:  [-3.  3.]


# Rounding :
# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
# E.g. round off to 1 decimal point, 3.16666 is 3.2

import numpy as np
arr = np.around([-3.16666],2)
print("rounding value: ",arr)       # rounding value:  [-3.17]


# floor :
# The floor() function rounds off decimal to nearest lower integer.
# E.g. floor of 3.166 is 3.

import numpy as np
arr = np.floor([-3.16666])
print("floor value: ",arr)       # floor value:  [-4]


# ceil :
# The ceil() function rounds off decimal to nearest upper integer.
# E.g. ceil of 3.166 is 4.

import numpy as np
arr = np.ceil([-3.16666])
print("ceil value: ",arr)       # ceil value:  [-3.]
