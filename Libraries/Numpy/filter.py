# it is work filtering.

import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)   # [41 43] because newarr take only true value.


# diract filtering from array.

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
filt_arr = arr % 2 == 0
new = arr[filt_arr]
print(new)      # [2 4 6 8]