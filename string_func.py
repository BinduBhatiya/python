# convert first character into capital.
# capitalize()

str = "hello world"
print(str.capitalize())                             # Hello world

# convert all capaital letter into small.
# casefold()

str = "HELLO World"
print(str.casefold())                               # hello world

# print string into center.
# center()

str = "hello"
print(str.center(20,"*"))                            # *******hello********
                                                     # 20 it means length of word

# count word how many time repeat.
# count()

str = "hello"
print(str.count('l'))                                # 2 

# find in which index, word is made
# find()

str = "hello python"
print(str.find('python'))                            # 6

# define the ending with this string or not.
# endswith()

str = "hello python"
print(str.endswith('python'))                         # true

# give extra tabs between character.
# expandtabs()

str = "h\te\tl\tl\to"
print(str)                                             # h	e	l	l	o
print(str.expandtabs())                                # h       e       l       l       o
print(str.expandtabs(2))                               # h e l l o
print(str.expandtabs(4))                               # h   e   l   l   o

# provide in which index character store.
# index()

str = "hello python"
print(str.index('y'))                                   # 7

# check it is alphanumeric or not.
# isalnum()

str = "hello12345"
print(str.isalnum())                                    # true

# check it is alphabet or not.
# isalpha()

str = "hellopython"                                     # str = "hello python" (false)
print(str.isalpha())                                    # true

# check it is decimal or not.
# isdecimal()

str = "37"
print(str.isdecimal())                                  # true

# check it is digit or not.
# isdigit()

str = "45456"
print(str.isdigit())                                    # true

# check variable is identifier or not.
# isidentifier()

str = "helloworld"
print(str.isidentifier())                               # true

# check the string is lowercas or not.
# islower()

str = "helloworld"
print(str.islower())                                    # true

# check is space or not in string.
# isspace()

str = "  "
print(str.isspace())                                    # true 

# check is title or not in string.
# istitle()

str = "Hello Python"                                    # str="hello python" (false)
print(str.istitle())                                    # true 

# check if character in uppercase or not.
# isupper()

str = "HELLO PYTHON"
print(str.isupper())                                    # true


# join any symbol where the value is separeted.
# join()

str = {"abc","xyz","pqr"}
symb = "||"
print(symb.join(str))                                   # xyz||abc||pqr

# if character is upprcase then convert into lowercase
# lower()

str = "HELLO PYTHON"
print(str.lower())                                      # hello python

# it is remove the space in leftside.
# lstrip()

str = "   Hello Python"
print(str.lstrip())                                     # Hello Python

# it is remove the space in rightside.
# rstrip()

str = "   Hello Python    "
print(str.rstrip())                                     #    Hello Python

# it is use to replace text 
# replace()

str = "this is demo. this is another demo."
print(str.replace("demo","text",2))                     # this is text. this is another text.

# it is define index where string is defined in last.
# rfind()

str = "this is demo. this is another demo. yet this is demo."
print(str.rfind("demo"))                                # 48

# it is define index where string is defined in last.
# rindex()

str = "this is demo. this is another demo. yet this is hour."
print(str.rindex("demo"))                                # 30

# it is cover all string with define argument.
# rjust()

str = "Hello Python."
print(str.rjust(25,"*"))                                # ************Hello Python.


# it is convert upper to lower and lower to upper.
# swapcase()

str = "Hello Python."
print(str.swapcase())                                   # hELLO pYTHON.

# it is write first character into uppercase.
# title()

str = "python is programming language."
print(str.title())                                      # Python Is Programming Language.

# it is convert character into uppercase.
# upper()

str = "python is programming language."
print(str.upper())                                      # PYTHON IS PROGRAMMING LANGUAGE.

# it is fill the string.
# zfill()

str = "Hello Python."
print(str.zfill(15))                                     # 00Hello Python.

# it is remove the space from both side.
# strip()

str = "    Hello Python.   "
print(str.strip())                                       # Hello Python.

# it is show in which index character is store.
# rindex()

str = "hello python"
print(str.rindex('o',2,11))                                # 10
print(str.find(" "))                                       # 5
print("find occurance",str.find("o"))                      # 4


# note :
# difference between index and find is if no value find in index then it will return "value error". whereas find return "-1" as an output.
# difference between index and rindex is in index define first occurance whereas rindex define last occurance.








