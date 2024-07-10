# variable should begin with alphabet or underscore.
abc=123
print('abc'.isidentifier())     #true

_=456
print('_'.isidentifier())       #true

# identifier can be alphanumerical but numbers should not be at the beggining
abc1234=5678
print('abc1234'.isidentifier())     #true

a1b2c3=123
print('a1b2c3'.isidentifier())      #true

# 1a2b3c=123
# print('1a2b3c'.isidentifier())    #false

# special character are not allowed in variable

# ab@c=123
# print('1a2b3c'.isidentifier())      #false

# ab c=123
# print('ab c'.isidentifier())      #false

ab_c=123
print('ab c'.isidentifier())        #true

ab_c = 123
print('ab c'.isidentifier())        #true

print('''hello
      world''')

print("hello \n world")

print(""" hello "world" """)  # if you want to print any word in double quotes then you can use """ . then it is give permission to use quotation. 

print('\\n')    #print \n in terminal






