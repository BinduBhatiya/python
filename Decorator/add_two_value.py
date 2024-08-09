def decorator(func):
    def wrapper(*args,**kwargs):
        print(f"executing {func.__name__} with arguments {args,kwargs}")
        result = func(*args,**kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
@decorator
def add(x,y):  
    return x+y
add(10,20)

@decorator
def mul(x,y):  
    return x*y
mul(10,20)  

@decorator
def div(x,y):  
    return x/y
div(400,20)  

# output :
'''
executing add with arguments ((10, 20), {})
add returned 30
executing mul with arguments ((10, 20), {})
mul returned 200
executing div with arguments ((400, 20), {})
div returned 20.0
'''