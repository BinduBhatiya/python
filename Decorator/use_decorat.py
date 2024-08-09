def decorator(func):
    def wrapper():
        print("hello python.")
        func()
        print("my name is krishna.")
    return wrapper
@decorator
def hello():
    print("how are you?")
hello()
    
# output :
'''
    hello python.
    how are you?
    my name is krishna.
'''