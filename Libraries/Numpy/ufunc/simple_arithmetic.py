# addition :
import numpy as np

arr1 = [1,2,3,4,5]
arr2 = [5,6,7,8,9]

newarr = np.add(arr1,arr2)
print("addition is: ",newarr)

# output :
# addition is:  [ 6  8 10 12 14]


# sustraction :
import numpy as np

arr1 = [1,2,3,4,5]
arr2 = [5,6,7,8,9]

newarr = np.subtract(arr1,arr2)
print("sustraction is: ",newarr)

# output :
# sustraction is:  [-4 -4 -4 -4 -4]


# multiplication :
import numpy as np

arr1 = [1,2,3,4,5]
arr2 = [5,6,7,8,9]

newarr = np.multiply(arr1,arr2)
print("multiplication is: ",newarr)

# output :
# multiplication is:  [ 5 12 21 32 45]



# Division :
import numpy as np

arr1 = [5,6,7,8,9]
arr2 = [1,2,3,4,5]

newarr = np.divide(arr1,arr2)
print("division is: ",newarr)

# output :
# division is:  [5.  3.  2.33333333  2.  1.8]


# power : power function is used to define the power of given value.

import numpy as np

arr1 = [1,2,3,4,5]
arr2 = [5,4,3,2,1]

pow_res = np.power(arr1,arr2)
print("power is: ",pow_res)

# output :
# power is:  [ 1 16 27 16  5]


# remainder() : it is used to define the reminder of any value.
# mod() : mod function also provide the reminder.

import numpy as np

arr1 = [5,6,7,8,9]
arr2 = [1,2,3,4,5]

rem_res = np.remainder(arr1,arr2)
print("reminder is: ",rem_res)

# output :
# reminder is:  [0 0 1 0 4]


# absolute() :
import numpy as np
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print("absolute value is: ",newarr)

# output :
# reminder is:  [0 0 1 0 4]

# divmod :
# The divmod() function return both the quotient and the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print("divmod is: ",newarr)

# output :
# divmod is:  (array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))
# first array is division value & second array is Modulus value.