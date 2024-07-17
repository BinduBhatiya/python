# EXERCISE :- 1. reverce string with the help of reverced() function.
str1 = 'hellopython'
rev = ''.join(reversed(str1))
print(rev)                                          # nohtypolleh
# it must use join() method. without using join() we can not print reverce string.



# EXERCISE :- 2. how to update character ? for ex : 'hello python' -> 'heplo python'
str2 = 'hello python'
print('original string: ',str2)

list1 = list(str2)
list1[2] = 'p'
str2 = ''.join(list1)
print('updating string at second index: ',str2)

# here we can use join() for join list into string.if we not use join then it can print list data like ['h','e','l'] but, if we use join() then it can print in string. 
# if we want to change entire string then we can take next same variable name then give value.
# output :
'''
    original string:  hello python
    updating string at second index:  heplo python
'''



# EXERCISE :- 3. how to delete single character in string ?
str3 = 'hello python'
print('original string : ',str3)
del_ch = str3[0:2] + str3[3:]
print('after deleting character : ',del_ch)

# output :
'''
    original string :  hello python
    after deleting character :  helo python
'''



# EXERCISE :- 4. how to delete entire string in python ?
str4 = 'hellopython'
del str4
#print(str4)

# Using "del" removes the variable "str4" from the current namespace, so any way it will result in a "NameError".


# EXERCISE :- 5. String formatting 
str5 = "{} {} {}".format('hello','python','world')
print('print string in default order : ',str5)
 
str5 = "{1} {0} {2}".format('hello','python','world')
print('print string with index order : ',str5)

str5 = "{w} {p} {h}".format(h='hello',p='python',w='world')
print('print string with key order : ',str5)

# output :
'''
    print string in default order :  hello python world
    print string with index order :  python hello world
    print string with key order :  world python hello
'''


# EXERCISE :- 6.  Integers such as Binary, hexadecimal, etc., and floats can be rounded or displayed in the exponent form with the use of format specifiers. 

# formatting of integer
str6 = "{0:b}".format(16)
print('binary representation of 16 is : ',str6)                 # 10000

# formatting of floats
str6 = "{0:e}".format(165.6458)
print('exponent representation of 165.6458 is : ',str6)         # 1.656458e+02

# rounding of integer
str6 = "{0:.2f}".format(1/6)
print('one-sixth is : ',str6)                                   # 0.17



# EXERCISE :- 7. A string can be left, right, or center aligned with the use of format specifiers, separated by a colon(:). The (<) indicates that the string should be aligned to the left, (>) indicates that the string should be aligned to the right and (^) indicates that the string should be aligned to the center. We can also specify the length in which it should be aligned. For example, (<10) means that the string should be aligned to the left within a field of width of 10 characters.

str7 = "|{:<10}|{:^10}|{:>10}|".format('hello','python','world')
print(str7)                                                         # |hello     |  python  |     world|

str7 = "{0:^16} was founded in {1:<4}!".format('hello,python',1989) 
print(str7)                                                         #   hello,python   was founded in 1989!



# EXERCISE :- 8. iterate character of a string.

str8 = 'python'
for i in str8:
    print(i,end=', ')                                               #  p, y, t, h, o, n,

str8 = 'python'
for i in range(0,len(str8)):
    print(str8[i],end=' ')                                          #  p y t h o n 



# EXERCISE :- 9. iterate character of a string in reverce order.

str9 = 'python'
for i in str9[::-1]:
    print(i,end=' ')                                                # n o h t y p


str9 = 'python'
for i in reversed(range(0,len(str9))):
    print(str9[i],end=' ')                                          # n o h t y p

