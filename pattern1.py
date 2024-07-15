'''
program 1 :-

1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''

for i in range(1,6):
    for j in range(i,6):
        print(i,end=' ')
    print("\n") 



'''
program 2 :-

1 
2 2 
3 3 3
4 4 4 4 
5 5 5 5 5 
'''   

for i in range(1,6):
    for j in range(0,i):
        print(i,end=' ')
    print("\n") 


'''
program 3 :-

        1 
      2 2 
    3 3 3
  4 4 4 4 
5 5 5 5 5 
''' 

for i in range(1,6):
    for k in range(5-i):
        print(" ",end=' ')
    for j in range(i):
        print(i,end=' ')
    print("\n") 


'''
program 4 :-

1 1 1 1 1
  2 2 2 2
    3 3 3
      4 4
        5
'''

for i in range(1,6):
    for k in range(i-1):
        print(" ",end=' ')
    for j in range(5-i+1):
        print(i,end=' ')
    print("\n") 