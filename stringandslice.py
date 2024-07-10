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
# syntax : var_nm[index_no]

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