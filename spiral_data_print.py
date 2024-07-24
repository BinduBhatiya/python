'''
1 2 3
4 5 6
7 8 9

[0][0]  [0][1]  [0][2]
[1][0]  [1][1]  [1][2]
[2][0]  [2][1]  [2][2]

'''
lst = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(1,2):
    for j in range(1,2):
        print(lst[i][j],end=' ')
        print(lst[i][j+1],end=' ')

for i in range(2,3):
    for j in range(2,3):
        print(lst[i][j],end=' ')
        print(lst[i][j-1],end=' ')
        print(lst[i][j-2],end=' ')

for i in range(1,2):
    for j in range(0,1):
        print(lst[i][j],end=' ')

for i in range(0,1):
    for j in range(0,1):
        print(lst[i][j],end=' ')
        print(lst[i][j+1],end=' ')
        print(lst[i][j+2],end=' ')

