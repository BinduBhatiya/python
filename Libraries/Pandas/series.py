# what is pandas series ?
# pandas series is similar to table column.it is used to hold single dimensional array of same type.

import pandas as pd
data = [1,2,3]
print("\nbasic use of pandas series :")
print(pd.Series(data))

# output :
'''
0    1
1    2
2    3
dtype: int64
'''


# Using Index.

import pandas as pd
data = [1,2,3]
var = pd.Series(data, index = ['day1','day2','day3'])
print("\nusing index : ")
print(var)

# output :
'''
day1    1
day2    2
day3    3
dtype: int64
'''

import pandas as pd
data = [1,2,3]
var = pd.Series(data, index = ['day1','day2','day3'])
print()
print(var['day3'])

# output :
# 3