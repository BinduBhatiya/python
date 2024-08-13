# convert datatype on existing array.
# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

# convert float into integer.

import numpy as np
arr = np.array([1.1, 2.1, 4.1])
new = arr.astype('int')
print(new)      # [1 2 4]
print(new.dtype)    # int32


# convert integer into boolean.

import numpy as np
arr = np.array([-1, 0, None])
newarr = arr.astype(bool)
print(newarr)       # [ True False  True]
print(newarr.dtype)     # bool