'''
 variable :
 In a programming language, Variables are words that are used to store values of any data type.
 syntax :
 variable_name = data values
 for Ex : num = 50
 Note :
 variable are mutable.
 In Python, we do not specify the data type for the variable. Python automatically understands which data type is being used and allocates memory space accordingly.
'''

# simple declaration and assign a value to the variable.

num = 10
numlist = [1, 3, 5, 7, 9]
str = 'Hello World'

print(num)                                         # 10
print(numlist)                                     # [1, 3, 5, 7, 9]
print(str)                                         # Hello World


# changing value of the variable.

val = 50
print("Initial value:", val)                        # Initial value: 50

val = 100   # assigning new value
print("Updated value:", val)                        # Updated value: 100


# assign multiple values to multiple variable.

name, age, city = 'David', 27, 'New York'

print(name)                                         # David
print(age)                                          # 27
print(city)                                         # New York


# we can also assign a single value to multiple variable.

a = b = 10
print('value of a: ',a)                             # value of a:  10
print('value of b: ',b)                             # value of b:  10



'''
constant :
A constant is a variable whose value cannot be modified.
for Ex : PI = 3.14
Note : 
constant are immutable.
'''

# define constant.

import constant as const
# it means fetch data of PI and GRAVITY from constant.py file
print('Value of PI:', const.PI)
print('Value of Gravitational force:', const.GRAVITY)



'''
Literal :
The data which is being assigned to the variables are called as Literal.
for Ex :
str = 'how are you Bindu?'  (it is a string Literal.)
Note :
Literal are mutable and immutable.
python support different type of Literal.like numeric literal,string literal,boolean literal,special literal etc.
'''

# Numeric Literals.
'''
Numeric Literals are values assigned to the Variables or Constants which cannot be changed i.e., they are immutable. There are a total of 3 categories in Numeric Literals. They are Integer, Float, and Complex.
'''

# Int Numeric Literal
a = 30

# Float Numeric Literal
b = 40.67

# Complex Numeric Literal
c = 10+4j

print(a)                                               # 30
print(b)                                               # 40.67
print(c)                                               # 10+4j
print(c.real, c.imag)                                  # 10.0 , 4.0

# string literals.
'''
A string literal is a series of characters surrounded by quotation marks. 
A single character surrounded by single or double quotations is also known as a character literal.
'''

string = 'Hello Guys'
multi_line = '''Hey
    There!!'''
char = 'Z'       

print(string)                                           # Hello Guys
print(multi_line)                                       # Hey
                                                             #There!! 
print(char)                                             # Z

# Boolean literal
'''
A Boolean Literal has either of the 2 values True or False. Where True is considered as 1 and False is considered as 0.
'''

x = True + 10
y = False + 50
print('value of x : ',x)                                 # value of x :  11
print('value of y : ',y)                                 # value of y :  50

# special literal :
''' 
Python provides a special kind of literal known as None.
'''

soap = "Available"
handwash = None

def items(x):
    if x == soap:
        print('Soap:', soap)
    else:
        print('Soap:', handwash)

items(soap)                                             # Soap: Available
items(handwash)                                         # Soap: None


# Literal Collection :
'''
there are four different type of Literal Collection. like List, Set, Tuple, Dictionary Literal.
'''

# List Literals 
'''
The elements in a list are of many data types. The values in the List are surrounded by square brackets ([]) and separated by commas (,). List values can be changed i.e., they are mutable.
'''

cars = ['Tata', 'BMW', 'Audi', 'Ferrari']
print(cars)                                             # ['Tata', 'BMW', 'Audi', 'Ferrari']

# Tuple Literals
'''
Just like a List, a tuple is also a collection of various data types. It is surrounded by parentheses () and each element is separated by a comma (,). It is immutable.
'''

num = (1, 2, 4, 5, 7, 8)
print(num)                                              # (1, 2, 4, 5, 7, 8)

# dict Literal
'''
The data is stored in the dictionary as a key-value pair. It is surrounded by curly braces {} and each pair is separated by commas (,). A dictionary can hold various types of data. Dictionaries are subject to change.
'''


student = {'Name':'David', 'Age':22, 'gen':'Male', 'City':'California', }
print(student)                                          # {'Name': 'David', 'Age': 22, 'gen': 'Male', 'City': 'California'}

print(student.keys())                                   # dict_keys(['Name', 'Age', 'gen', 'City'])
print(student.values())                                 # dict_values(['David', 22, 'Male', 'California'])


# Set Literal
'''
Set is an unordered data set collection. It is surrounded by and each element is separated by a comma (,).
'''

chars = {'a', 'b', 'a', 'e', 'z', 'z', 'x'}
print(chars)  # Sets has no duplicate elements          # {'e', 'x', 'a', 'z', 'b'}


