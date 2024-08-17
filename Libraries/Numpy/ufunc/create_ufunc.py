# create addition by using own universal function.

import numpy as np
def myadd(a,b):
    return a + b
myadd = np.frompyfunc(myadd,2,1)
print("addition using own ufunc: ",myadd([1,2,3,4], [5,6,7,8]))


# check the type of "universal function".

# add()
import numpy as np
print("type of function: ",type(np.add))

# output :
# type of function:  <class 'numpy.ufunc'>

# concatenate()
import numpy as np
print("type of function: ",type(np.concatenate))

# output :
# type of function:  <class 'numpy.ufunc'>

# check condition is the function is ufunc or not.
import numpy as np

if type(np.add) == np.ufunc:
    print("the function is universal function.")
else:
    print("the function is not universal function.")

# output :
# the function is universal function.

    