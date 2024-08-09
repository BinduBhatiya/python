# what is the difference between copy and view.

# use copy() method.
import numpy as np
arr = np.array([1,2,3,4,5])
new = arr.copy()
arr[0] = 99
print("original value: ",arr)
print("copy value: ",new)

# output :
'''
original value:  [99  2  3  4  5]
copy value:  [1 2 3 4 5]
'''


# use view() method.
import numpy as np
arr = np.array([1,2,3,4,5])
new = arr.view()
arr[0] = 99
print("original value: ",arr)
print("copy value: ",new)

# output :
'''
original value:  [99  2  3  4  5]
copy value:  [99  2  3  4  5]
'''


# use .base method.
import numpy as np
arr = np.array([1,2,3,4,5])
new1 = arr.view()
new2 = arr.copy()

print("view: ",new1.base)
print("copy: ",new2.base)

# output :
'''
view:  [1 2 3 4 5]
copy:  None
'''