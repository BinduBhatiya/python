# HOW TO ROW WISE SUM OF NESTED LIST
'''
    like :

    [ [1,2,3],
      [4,5,6],
      [7,8,9]
    ]

    1+2+3 = 6
    4+5+6 = 15
    7+8+9 = 24 
'''

def row_sum(lst):
    res = []
    for i in range(len(lst)):
        sum = 0
        for j in range(len(lst)):
            sum+=lst[i][j]
        res.append(sum)
    return res
lst = [[1,2,3], [4,5,6], [7,8,9]]
print(row_sum(lst))


# OUTPUT :
# [6, 15, 24]


# METHOD 1 :
# HOW TO COLUMN WISE SUM OF NESTED LIST
'''
    like :

    [ [1,2,3],
      [4,5,6],
      [7,8,9]
    ]

    1+4+7 = 12
    2+5+8 = 15
    3+6+9 = 18
'''

def column_sum(lst):
    res = []
    for i in range(len(lst)):
        sum = 0
        for j in range(len(lst)):
            sum+=lst[j][i]
        res.append(sum)
    return res
lst = [[1,2,3], [4,5,6], [7,8,9]]
print(column_sum(lst))

# OUTPUT :
# [12, 15, 18]


# METHOD 2 (using map, zip function):
def column_sum(lst):
    return list(map(sum, zip(*lst)))
lst = [[1,2,3], [4,5,6], [7,8,9]]
print(column_sum(lst))

# OUTPUT :
# [12, 15, 18]


# METHOD 3 (using list comprehension):
def column_sum(lst):
    return [sum(i) for i in zip(*lst)] 
lst = [[1,2,3], [4,5,6], [7,8,9]]
print(column_sum(lst))

# OUTPUT :
# [12, 15, 18]
