# find palindrome number or not like 121 is palindrome number.
# reverce number of actual value both are same it is palindrome number.


num = int(input('enter the number : '))
sum = 0
c = num
while(num > 0):
    rem = num % 10
    sum = sum * 10 + rem
    num = num // 10
if c == sum:
    print(c,' is palindrome number.') 
else:
    print(c,' is not palindrome number.') 


# output :
'''
    enter the number : 121
    121  is palindrome number.
    enter the number : 153
    153  is not palindrome number.
'''