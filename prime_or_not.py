# find prime number or not

num = int(input('enter the number: '))
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print(num, 'is prime number.')
else:
    print(num, 'is not prime number.')



# output : 
'''
    enter the number: 13
    13 is prime number.

    enter the number: 12
    13 is not prime number.
'''