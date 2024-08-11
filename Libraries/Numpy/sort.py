# sorted numpy array.

import numpy as np
arr = np.array([4,2,5,1,3])
srt = np.sort(arr)
print(srt)      # [1 2 3 4 5]


import numpy as np
arr = np.array([True, False, True])
srt = np.sort(arr)
print(srt)      # [False, True, True]


import numpy as np
arr = np.array(['banana', 'apple', 'cherry'])
srt = np.sort(arr)
print(srt)      # ['apple', 'banana', 'cherry']


import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

# output :
'''
[[2 3 4]
 [0 1 5]]
'''