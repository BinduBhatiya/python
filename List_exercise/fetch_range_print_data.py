# fetch the range from user and print the data

# METHOD 1 (using simple for loop) :
 
r1 = int(input("enter the first range: "))
r2 = int(input("enter the second range: "))

lst = []
for i in range(r1,r2+1):
    lst.append(i)
print(lst)

# OUTPUT :
'''
    enter the first range: 1
    enter the second range: 5
    [1, 2, 3, 4, 5]
'''


# METHOD 2 (using map,Lambda function) :

def fetch_range(r1,r2):
    return list(map(lambda i: i,range(r1,r2+1)))
print(fetch_range(1,5))                                             # [1, 2, 3, 4, 5]



# METHOD 3 (using List comprehension) :

def fetch_range(r1,r2):
    return list(item for item in range(r1,r2+1))
r1,r2 = 1,5
print(fetch_range(r1,r2))                                              # [1, 2, 3, 4, 5]                                             
