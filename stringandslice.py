# string is immutable
# string is denoted with : 's', "s", '''s''', """s"""

# using single quotes
s = 'hello python'
print(type(s))                              # <class 'str'>

s1 = '@#$%&*'
print(type(s1))                             # <class 'str'>

# using double quotes
s = "hello how are you?"
print(type(s))                              # <class 'str'>

s1 = "i'm fine"
print(type(s1))                             # <class 'str'>

# using triple single quotes
s = '''life is beautiful'''
print(type(s))                              # <class 'str'>

s1 = '''python is high level programming language'''
print(type(s1))                             # <class 'str'>

# using triple double quotes
s = """python was developed in 1989."""
print(type(s))                              # <class 'str'>

s1 = """founder of python is gudo wan rusom"""
print(type(s1))                             # <class 'str'>


# using str()
s = str('python')
print(s)                                    # python
print(type(s))                              # <class 'str'>


#string has len() function which is used to get number of character present in a string
s = 'hello'
print(len(s))                               # 5

s1 = 'python world'
print(len(s1))                              # 12


# INDEXING is the process of extracting single character from string.
# indexing can be done in two way : positive indexing, negative indexing
# syntax : var_nm[start: stop: step]

# positive indexing
s = "hello world"
print(s[1])                                 # e

# negative indexing
s = "hello world"
print(s[-3])                                # r

# hello world (positive)
# 012345678910

#  h  e  l l o   w o r l d (negative)
# -11-10-9-8-7-6-5-4-3-2-1 

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

slice = my_tuple[::2]
print(slice)                                # (1, 3, 5, 7, 9,11)

slice = my_tuple[5:10]
print(slice)                                # (6, 7, 8, 9, 10)

slice = my_tuple[:10]
print(slice)                                # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

slice = my_tuple[5:]
print(slice)                                # (6, 7, 8, 9, 10, 11)

slice = my_tuple[:]
print(slice)                                # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

slice = my_tuple[-8:-3]
print(slice)                                # (4, 5, 6, 7, 8)

slice = my_tuple[5::2]
print(slice)                                # (6, 8, 10)

slice = my_tuple[::-1]
print(slice)                                # (11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)


# positive slicing with three argument
s1 = 'republic day'
print(s1[2:5:1])                            # pub

print(s1[7:13:2])                           # cdy

print(s1[1:9:3])                            # ecb

print(s1[0:9:4])                            # rb

print(s1[0::11])                            # ry


# negative slicing with three argument
s = 'python world'
print(s[-1:-13:-1])                            # dlrow nohtyp

print(s[-3:-6:-1])                             # row

print(s[-8:-13:-2])                            # otp

print(s[-1:-8:-3])                             # don

print(s[-2:-11:-2])                            # lo ot

print(s[-5:-12:-3])                            # cwoy

print(s[-4:-13:-4])                            # oop

print(s[-4:-11:-3])                            # ont


# mix slicing positive and negative
s = 'python world'
print(s[-12:-6:1])                            # python

print(s[-9:9:])                               # hon wo

print(s[9:5:1])                               # 

print(s[-12:-6:-1])                           # 

print(s[-5:-0:-1])                            # w nohty

print(s[10:-10:-2])                           # lo o
