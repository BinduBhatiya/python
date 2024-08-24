# what is dataframe ?
'''
    dataframe is a two dimension data structure.like a two dimensional array or table with row and column.
'''


import pandas as pd
mydataset = {
    'cars' : ['THAR', 'BMW', 'JAGUAR'],
    'gares' : [4,6,9]
}
myvar = pd.DataFrame(mydataset)         # simple use of dataframe.
print("\nsimple use of DataFrame : ")
print(myvar)


# output :
'''
     cars    gares
0    THAR      4
1     BMW      6
2  JAGUAR      9
'''



# locate Row :
'''
As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)
'''

import pandas as pd 
mydataset = {
    'cars' : ['Thar', 'BMW', 'audi'],
    'gares' : [4, 6, 8]
}
var = pd.DataFrame(mydataset)
print("\nsingle dimensional array : ")
print(var.loc[0])       # single dimension array


# output :
'''
cars     Thar
gares       4
Name: 0, dtype: object
'''


import pandas as pd
mydataset = {
    'cars' : ['Thar', 'BMW', 'Jaguar'],
    'gares' : [4, 6, 8]
}
var = pd.DataFrame(mydataset)
print()
print(var.loc[[0]])


# output :
'''
   cars  gares
0  Thar      4
'''


import pandas as pd
mydataset = {
    'cars' : ['Thar', 'BMW', 'Audi'],
    'gares' : [4, 6, 8]
}
var = pd.DataFrame(mydataset)
print("\nTwo dimensional array : ")
print(var.loc[[0, 1]])         # Two dimensional array 


# output :
'''
   cars   gares
0  Thar      4
1   BMW      6
'''


# Named Indexes :
# with the index argument you can named your own indexes.

import pandas as pd 
mydataset = {
    'cars' : ['Thar', 'BMW', 'I20'],
    'gares' : [4, 6, 8]
}
var = pd.DataFrame(mydataset, index=["day1", "day2", "day3"])
print("\nnamed indexes : ")
print(var.loc[["day2"]])


# output :
'''
      cars  gares
day2  BMW      6
'''