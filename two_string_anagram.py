# Determine if two strings are anagrams of each other (contain the same characters in the same frequency)

# METHOD 1

str1 = 'listen'
str2 = 'silent'

lst1 = list(str1)
lst1.sort()

lst2 = list(str2)
lst2.sort()

if lst1 == lst2:
    print('true')
else:
    print('false')

# METHOD 2

"""str1 = 'listen'
str2 = 'silent'

lst1=sorted(str1)
lst2=sorted(str2)

if lst1 == lst2:
    print('true')
else:
    print('false')"""