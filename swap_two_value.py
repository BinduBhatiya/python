# swapping two values
# METHOD 1 (with using third variable )

num1 = int(input('enter the first value: '))
num2 = int(input('enter the second value: '))

print('before swapping : ')
print('num1 = ',num1)
print('num2 = ',num2)

num3 = num1
num1 = num2
num2 = num3

print('after swapping : ')
print('num1 = ',num1)
print('num2 = ',num2)


# METHOD 2 (without using third variable)

a = int(input('enter the first value: '))
b = int(input('enter the second value: '))

print('before swapping : ')
print('a = ',a)
print('b = ',b)

a = a + b
b = a - b
a = a - b 

print('after swapping : ')
print('a = ',a)
print('b = ',b)



# output :
'''
    enter the first value: 10
    enter the second value: 20

    before swapping :
    num1 =  10
    num2 =  20
    
    after swapping :
    num1 =  20
    num2 =  10
'''

