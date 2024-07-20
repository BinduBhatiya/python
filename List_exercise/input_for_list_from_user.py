# fetch data from user for List

lst = []
itm = int(input('enter the value for how many item you want to print : '))
for i in range(itm):
    data = int(input())
    lst.append(data)
print(lst)


# OUTPUT :
'''
    enter the value for how many item you want to print : 3
    1
    2
    3
    [1, 2, 3]
'''


# METHOD 2 :

n = int(input('enter the number : '))
a = list(map(int,input('enter the value : ').split()))[:n]

print('list is: ',a)

# OUTPUT :
'''
    enter the number : 3
    enter the value : 10 20 30
    list is:  [10, 20, 30]
'''