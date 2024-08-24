# what is pandas series ?
# pandas series is similar to table column.it is used to hold single dimensional array of same type.

import pandas as pd
data = [1,2,3]
print(pd.Series(data))

# output :
'''
0    1
1    2
2    3
dtype: int64
'''