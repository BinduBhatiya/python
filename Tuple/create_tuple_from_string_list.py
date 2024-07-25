# HOW TO CREATE A TUPLE FROM "STRING" AND "LIST".

lst = ['python','world']
str1 = 'hello'

tup = tuple([str1] + lst)
print(tup)                          # ('hello', 'python', 'world')