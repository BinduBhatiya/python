# Data type :
'''
    1. data type are the type of value.

    2. There are six type of data type in python.
        1. Numeric 
            -> Integer
            -> Float
            -> Complex Number
        2. Dictionary
        3. Boolean
        4. Set
        5. Sequence Type
            -> Strings
            -> List
            -> Tuple
        6. Binary Types
            -> memoryview
            -> bytearray
            -> bytes

    3. This data type devide in two way.
        1. mutable                  2. immutable
          -> List                     -> Integer
          -> Dictionary               -> Float
          -> byte Array               -> complex
                                      -> String
                                      -> Tuple
                                      -> Set                               
'''

# Numeric Data Types :
# The numeric data type in Python represents the data that has a numeric value. A numeric value can be an integer, a floating number, or even a complex number.
# this code define the type of value.

a = 5
print("Type of a: ", type(a))                       # Type of a:  <class 'int'>

b = 5.0
print("Type of b: ", type(b))                       # Type of b:  <class 'float'>

c = 2 + 4j
print("Type of c: ", type(c))                       # Type of c:  <class 'complex'>


# Sequence Data Types :
# The sequence Data Type in Python is the ordered collection of similar or different Python data types. Sequences allow storing of multiple values in an organized and efficient fashion.

String1 = 'Welcome to the python World'
print("String with the use of Single Quotes: ")
print(String1)
String1 = "I'm a python"
print("String with the use of Double Quotes: ")
print(String1)
print(type(String1))
String1 = '''I'm a python and I am a programming "Language"'''
print("String with the use of Triple Quotes: ")
print(String1)
print(type(String1))

String1 = '''hello 
             python 
             world'''
print("Creating a multiline String: ")
print(String1)

# output :
'''
1. String with the use of Single Quotes: 
Welcome to the python World

2. String with the use of Double Quotes: 
I'm a python

<class 'str'>

3. String with the use of Triple Quotes: 
I'm a python and I am a programming "Language"

<class 'str'>

4. Creating a multiline String: 
            hello 
            python 
            world
'''


# List Data type :
# List are just like arrays, declared in other languages which is an ordered collection of data. It is very flexible as the items in a list do not need to be of the same type.  

List = []
print("Initial blank List: ")
print(List)
List = ['hello python']
print("List with the use of String: ")
print(List)
List = ["hii", "hello", "python"]
print("List containing multiple values: ")
print(List[0])
print(List[2])
List = [['hello', 'pyhton'], ['world']]
print("Multi-Dimensional List: ")
print(List)


# output :
'''
Initial blank List: 
[]

List with the use of String: 
['hello python']

List containing multiple values: 
hii
python

Multi-Dimensional List: 
[['hello', 'pyhton'], ['world']]
'''


# Tuple Data Type
# Just like a list, a tuple is also an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable i.e. tuples cannot be modified after it is created. It is represented by a tuple class.  

Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)
Tuple1 = ('hello', 'python')
print("Tuple with the use of String: ")
print(Tuple1)
list1 = [1, 2, 4, 5, 6]
print("Tuple using List: ")
print(tuple(list1))
Tuple1 = tuple('python')
print("Tuple with the use of function: ")
print(Tuple1)
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'django')
Tuple3 = (Tuple1, Tuple2)
print("Tuple with nested tuples: ")
print(Tuple3)


# output :
'''
Initial empty Tuple: 
()

Tuple with the use of String: 
('hello', 'python')

Tuple using List: 
(1, 2, 4, 5, 6)

Tuple with the use of function: 
('p', 'y', 't', 'h', 'o', 'n')

Tuple with nested tuples: 
((0, 1, 2, 3), ('python', 'django'))
'''

# Boolean Data Type
# Python Data type with one of the two built-in values, True or False.

print(type(True))               # <class 'bool'>
print(type(False))              # <class 'bool'>
# print(type(true))               # NameError: name 'true' is not defined. Did you mean: 'True'?


# Set Data Type
# a Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. 

set1 = set()
print("Initial blank Set: ")
print(set1)
set1 = set("hellopython")
print("Set with the use of String: ")
print(set1)
set1 = set(["python", "For", "python"])
print("Set with the use of List: ")
print(set1)
set1 = set([1, 2, 'python', 4, 'For', 6, 'world'])
print("Set with the use of Mixed Values")
print(set1)

# output :
'''
Initial blank Set: 
set()

Set with the use of String: 
{'p', 'l', 'y', 'n', 'o', 'e', 't', 'h'}

Set with the use of List: 
{'python', 'For'}

Set with the use of Mixed Values
{1, 2, 'world', 4, 6, 'For', 'python'}
'''

set1 = set(["python","is","python"])
print("initial set : ")
print(set1)
print("elements of set : ")
for i in set1:
    print(i,end=" ")
print("python" in set1)

# output :
'''
initial set : 
{'python', 'is'}
elements of set : 
python  is
True
'''


# Dictionary Data Type
# A dictionary in Python is an unordered collection of data values, used to store data values like a map, unlike other Python Data Types that hold only a single value as an element, a Dictionary holds a key: value pair. 

Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict = {1: 'hello', 2: 'python', 3: 'world'}
print("Dictionary with the use of Integer Keys: ")
print(Dict)
Dict = {'Name': 'python', 1: [1, 2, 3, 4]}
print("Dictionary with the use of Mixed Keys: ")
print(Dict)
Dict = dict({1: 'hello', 2: 'python', 3: 'world'})
print("Dictionary with the use of dict(): ")
print(Dict)
Dict = dict([(1, 'python'), (2, 'world')])
print("Dictionary with each item as a pair: ")
print(Dict)


# output :
'''
Empty Dictionary: 
{}

Dictionary with the use of Integer Keys: 
{1: 'hello', 2: 'python', 3: 'world'}

Dictionary with the use of Mixed Keys: 
{'Name': 'python', 1: [1, 2, 3, 4]}

Dictionary with the use of dict(): 
{1: 'hello', 2: 'python', 3: 'world'}

Dictionary with each item as a pair: 
{1: 'python', 2: 'world'}
'''


# access data using key name and .get() method

Dict = {1: 'hello', 'name': 'python', 3: 'world'}
print("Accessing a element using key:")
print(Dict['name'])
print("Accessing a element using get:")
print(Dict.get(3))

# output :
'''
Accessing a element using key:
python
Accessing a element using get:
world
'''




