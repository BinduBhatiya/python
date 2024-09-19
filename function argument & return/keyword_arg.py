# there are four types of function argument.
'''
    1. default argument
    2. keyword argument
    3. variable_length argument
    4. required argument

    it is a keyword argument.
    
    in which we can provide argument with key = value, this way the interpreter recognizes the argument by the 
    parameter name. hence, the order in which argument are passed no matter.
'''

def average(a,b):
    print('the average is: ',(a+b)/2)               # the average is:  5.0
average(b=1, a=9) 


def greet(name,greeting = 'hello'):
    print(f'{greeting}  {name}')
greet('Bindu')                      # hello Bindu
greet('lakhu','hii')                # hii lakhu
greet('krishna','hey')              # hey krishna


# arbitary keyword argument.

def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')
print_info(name='bindu',age=20,salary=15000)

# output :
'''
    name : bindu
    age : 20
    salary : 15000
'''

# combining positional and keyword argument.

def describe_pet(pet_name, animal_type="dog", **kwargs):
    description = f"I have a {animal_type} named {pet_name}."
    for key, value in kwargs.items():
        description += f" {key.capitalize()}: {value}."
    print(description)

describe_pet("Buddy", age=5, color="brown")

# output :
# I have a dog named Buddy. Age: 5. Color: brown.
