'''
A return statement is used to end the execution of the function call and “returns” the result to the caller.
'''

# return single value

def add(a, b):
    return a + b
result = add(2, 3)
print(result)   # result is 5

# return multiple value

def min_max(number):
    return min(number), max(number)
min_num,max_num = min_max([1,2,3,4,5])
print(min_num)  # 1
print(max_num)  # 5         


# no return value

def messege_box(message):
    print(message)
    # return message
result = messege_box('hello')
print(result)           # None


# return a datastructure.
# A function can return complex data structures like lists, dictionaries, or custom objects.

def info(name,age):
    return {'name':name,'age':age}
res = info('Bindu',20)
print(res)          # {'name': 'Bindu', 'age': 20} 


# return multiple value.

def add(a, b):
    return a + b
def is_true(a):
    return bool(a)
res = add(2, 3)
#print("Result of add function is {}".format(res))       # Result of add function is 5
print("Result of add function is", res)                  # Result of add function is 5
res = is_true(2<5)
print("\nResult of is_true function is {}".format(res))     # Result of is_true function is True


# return multiple values using tuple.

def fun(): 
    str = "geeksforgeeks"
    x = 20
    return str, x;  # Return tuple, we could also 
                    # write (str, x) 
str, x = fun()  
print(str)      # geeksforgeeks
print(x)        # 20


# return multiple values using list.

def fun(): 
    str = "geeksforgeeks"
    x = 20   
    return [str, x];   

list = fun()  
print(list)   # [geeksforgeeks, 20]

# return multiple values using dictionary.

def fun(): 
    d = dict();  
    d['str'] = "GeeksforGeeks"
    d['x']   = 20
    return d 

d = fun()  
print(d)    # {'str': 'GeeksforGeeks', 'x': 20}




