# armstrong number
# like 153 is armstrong number.
# for ex: (1*1*1 + 5*5*5 + 3*3*3) = 153

num = int(input('enter the number : '))
s = 0
c = num
while(num > 0):
    r = num % 10
    s = (r*r*r) + s
    num = num // 10
if c == s:
    print(c,' is armstrong number.')
else:
    print(c,' is not armstrong number.')


# output :
'''
    enter the number : 153
    153  is armstrong number.
    
    enter the number : 111
    111  is not armstrong number.
'''
 