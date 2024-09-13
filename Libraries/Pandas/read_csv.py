# using "to_string".

import pandas as pd

df = pd.read_csv('Book1.csv')
print('Method 1:')
print(df.to_string())

# output :
'''
      name  age
0    lakhu   10
1  krishna   20
2  ganesha   30
'''

# using "only variable."

import pandas as pd
df = pd.read_csv('Book1.csv')
print('\nMethod 2:')
print(df)

# output :
'''
      name  age
0    lakhu   10
1  krishna   20
2  ganesha   30
'''

# using "options.display.max_rows" object.

import pandas as pd
print('\nMethod 3:')
print(pd.options.display.max_rows)        # 60



# Increase the maximum number of rows to display the entire DataFrame

import pandas as pd
pd.options.display.max_rows = 3
df = pd.read_csv('book1.csv')
print('\nMethod 4:')
print(df)


# output :
'''
     name  age
0   lakhu   10
..    ...  ...
4    Neha   10

[5 rows x 2 columns]
'''