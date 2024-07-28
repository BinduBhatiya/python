# acos() :
# return the arc cosine of different numbers.

import math
print(math.acos(0.55))          # 0.9884320889261531
print(math.acos(-0.55))         # 2.15316056466364
print(math.acos(0))             # 1.5707963267948966
print(math.acos(1))             # 0.0
print(math.acos(-1))            # 3.141592653589793



'''
    1. The math.acos() method returns the arc cosine value of a number.

    2. The parameter passed in math.acos() must lie between -1 to 1.

    3. math.acos(-1) will return the value of PI.
'''


# acosh() :
# Return the inverse hyperbolic cosine of different numbers

import math
print (math.acosh(7))               # 2.6339157938496336
print (math.acosh(56))              # 4.71841914237288
print (math.acosh(2.45))            # 1.5447131178707394
print (math.acosh(1))               # 0.0


'''
    1. The math.acosh() method returns the inverse hyperbolic cosine of a number.

    2. Note: The parameter passed in acosh() must be greater than or equal to 1.
'''

# cos() :
# Return the cosine of different numbers
import math

print (math.cos(0.00))                  # 1.0
print (math.cos(-1.23))                 # 0.3342377271245026
print (math.cos(10))                    # -0.8390715290764524
print (math.cos(3.14159265359))         # -1.0


# cosh() :
# Return the hyperbolic cosine of different numbers

import math
print (math.cosh(1))                # 1.5430806348152437
print (math.cosh(8.90))             # 3665.986837772461
print (math.cosh(0))                # 1.0
print (math.cosh(1.52))             # 2.3954685410471868