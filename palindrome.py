# find palindrome number or not like 121 is palindrome number.
# reverce number of actual value both are same it is palindrome number.


n = int(input('enter the number : '))
s = 0
c = n
while(n > 0):
    r = n % 10
    s = s * 10 + r
    n = n // 10
if c == s:
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