# print the data of List .

# METHOD 1 (using for loop) :
lst = [1,2,3,4,5]
for i in range(len(lst)):
    print(lst[i],end=' ')                                         # 1 2 3 4 5 


# METHOD 2 (using while loop) :
lst = [1,2,3,4,5]
i = 0
while i < len(lst):
    print(lst[i],end=' ')                                         # 1 2 3 4 5
    i+=1


# METHOD 3 (using map function) :
def fetch_data():
    lst = [1,2,3,4,5]
    return list(map(lambda x: x, lst))
print(fetch_data())                                                 # [1, 2, 3, 4, 5]


# METHOD 4 (iterate multiple list using zip() function) :
lst1 = [1,2,3]
lst2 = ['p','q','r']

for i1,i2 in zip(lst1,lst2):
    print(i1,"->",i2)

# OUTPUT :
'''
    1 -> p
    2 -> q
    3 -> r  
'''


# METHOD 5 (using iter(), next() function) :
lst = [1,2,3,4,5]
iterator = iter(lst)
try:
    while True:
        element = next(iterator)
        print(element)
except:
    pass

# OUTPUT :
'''
    1
    2
    3
    4
    5
'''
