# there are four types of function argument.
'''
    1. default argument
    2. keyword argument
    3. variable_length argument
    4. required argument
'''
'''
A default argument is an argument that has a default value specified in the function definition.
If the caller does not provide a value for that argument, the default value will be used.
'''
# it is a default argument.

def average(a=9,b=1):
    print('the average is: ',(a+b)/2)               # the average is:  3.0
average(1,5)                                        # here, it is take 1,5 value.if we not pass 1,5 then it take 9,1 values.


# for ex:
def average(a=9,b=1):
    print('the average is: ',(a+b)/2)               # the average is:  5.0
average()


def average(a=9,b=1):
    print('the average is: ',(a+b)/2)               # the average is:  9.0
average(b=9)                                        # here, it is take b=9 rather than b=1.


def name(fname, mname = "Bindu", lname = "Merubhai"):
    print('my name is: ',fname,mname,lname)         # my name is:  Bhatiya Bindu Merubhai
name('Bhatiya')