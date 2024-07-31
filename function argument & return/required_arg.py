# there are four types of function argument.
'''
    1. default argument
    2. keyword argument
    3. variable_length argument
    4. required argument
'''
# it is a required argument.
# A required argument in Python is an argument that must be provided when a function is called. If you not give value to  argument, Python raises a TypeError.

def demo(name):
    print(f'hello {name}')
demo('Bindu')   # hello Bindu
demo()          # TypeError: demo() missing 1 required positional argument: 'name'

 