# what is decorator ?
'''
    decorator is a function which is used another function as an argument. and then it is called multiple function.
    in which we must define "@decorator" for calling function.
    in decorator we must define wrapper() function. with the help of wrapper function we can print function data. 
'''


def decorator(hello2):
    def wrapper():      # here, wrapper() function is not built-in but it is user-defined function.But, it is must required to define. without defining this function compiler throw typeerror.
        print("hello python.")
        hello2()
        print("my name is krishna.")
    return wrapper
@decorator
def hello():
    print("how are you?")
hello()
@decorator
def hello1():
    print("how are you....?")
hello1()
    
# output :
'''
    hello python.
    how are you?
    my name is krishna.

    hello python.
    how are you....?
    my name is krishna.
'''