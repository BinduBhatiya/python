# FIND THE LENGTH OF LIST IN DIFFERENT WAY

# METHOD 1 (using enumerator) :
lst = [11,22,33]
sum = 0
for i,a in enumerate(lst):
    sum += 1
print('length of list is : ',sum)                                   # 3     

# SUMMARY :
'''
here, enumerate is a built in function. it can fetch data from list with index. here we can give two variable like 'i' and 'a'.
in which i can store 'index value' where as a fetch the value.

syntax :
enumerate(iterable,start=0)
'''


# METHOD 2 (using len() function) :
lst = [11,22,33]
print('length of list is : ',len(lst))                              # 3 
    




