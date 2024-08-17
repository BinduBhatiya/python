# without using ufunc we can add two value.

a = [1,2,3,4,5,6,7]
b = [1,2,3,4,5,6,7]
c = []
for i,j in zip(a,b):
    c.append(i+j)
print("without using ufunc: ",c)     


# numpy has universal function "add()" it return same result.

import numpy as np
a = [1,2,3,4,5,6,7]
b = [1,2,3,4,5,6,7]
print("using ufunc: ",np.add(a,b))
