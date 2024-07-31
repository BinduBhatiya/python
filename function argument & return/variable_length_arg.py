# there are four types of function argument.
'''
    1. default argument
    2. keyword argument
    3. variable_length argument
    4. required argument
'''
# it is a variable_length argument.

'''
    There are two types of variable-length arguments:

    1. Variable-length positional arguments (*args)
    2. Variable-length keyword arguments (**kwargs)
'''

# positional argument.

def sum_all(*args):
    total = sum(args)
    return total
print(sum_all(1,2,3,4,5))               # 15


# arbitary keyword argument.

def print_info(**kwargs):
    print(kwargs.items())       # dict_items([('name', 'bindu'), ('age', 20), ('salary', 15000)])
    for key,value in kwargs.items():
        print(f'{key} : {value}')
print_info(name='bindu',age=20,salary=15000)

# output :
'''
    name : bindu
    age : 20
    salary : 15000
'''

# combining positional,keyword,variable_length argument.

def example_function(arg1, arg2, *args, kwarg1="default", **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

example_function(1, 2, 3, 4, 5, kwarg1="not default", kwarg2="extra", kwarg3="additional")

# Output:
'''
    arg1: 1
    arg2: 2
    args: (3, 4, 5)
    kwarg1: not default
    kwargs: {'kwarg2': 'extra', 'kwarg3': 'additional'}
'''
