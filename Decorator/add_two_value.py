# how to perform arithmetic operation using decorator.

def decorator(func):
    def wrapper(*args,**kwargs):
        print(f"executing {func.__name__} with arguments {args,kwargs}")
        result = func(*args,**kwargs)
        print(f"{func.__name__} returned {result}")
        # print(f"result is: {result}")
        return result
    return wrapper
@decorator
def addition(x,y):  
    return x+y
addition(10,20)

@decorator
def multiplication(x,y):  
    return x*y
multiplication(10,20)  

@decorator
def division(x,y):  
    return x/y
division(400,20)  

# output :
'''
executing addition with arguments ((10, 20), {})
addition returned 30
executing multiplication with arguments ((10, 20), {})
multiplication returned 200
executing division with arguments ((400, 20), {})
division returned 20.0
'''