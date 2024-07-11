# count vowels in a string

str1 = 'aeiouAEIOU'
str2 = 'hello world'

count = 0
for char in str2:
    if char in str1:
        count+=1
print(count)
    