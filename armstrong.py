# armstrong number
# like 153 is armstrong number.
# for ex: (1*1*1 + 5*5*5 + 3*3*3) = 153

num = int(input('enter the number : '))
sum = 0
c = num
while(num > 0):
    rem = num % 10
    sum = (rem*rem*rem) + sum
    num = num // 10
if c == sum:
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
 