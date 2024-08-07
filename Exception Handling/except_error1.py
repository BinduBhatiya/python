# except error handling.

a = int(input("enter first number: "))
b = int(input("enter second number: "))
try:
    c = a / b
    print(" division is: ",c)
except:
    print("not divided value.")
else:
    print("division successful.")


# output :
'''
1st Run:
    enter first number: 20
    enter second number: 0
    not divided value.
    
2nd Run:
    enter first number: 10
    enter second number: 2
    division is:  5.0
    division successful.
'''