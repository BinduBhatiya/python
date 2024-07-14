# print fibonacci series 
# 0 1 1 2 3 5.....


no = int(input("enter length of fibonacci series : "))
num1 = 0
num2 = 1
print('fibonacci series is: ',num1,num2,end=' ')
# print(num1)
# print(num2)
for i in range(2,no+1):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    
    print(num3,end=' ')

# output :
'''
        enter length of fibonacci series : 5
        fibonacci series is:  0 1 1 2 3 5 
'''