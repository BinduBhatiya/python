# CONCATE STRING DEFINE IN LIST

# METHOD 1 :
lst = ['hello', 'python', 'world']
res = ' '.join(map(str,lst))
print(res)                                              # hello python world

# METHOD 2 :
def func(lst):
    return lst
lst = ['hello', 'python', 'world']
res = ' '.join(list(map(func,lst)))
print(res)                                              # hello python world

# METHOD 3 :
def func(lst):
    res = ' '.join(list(map(func,lst)))
lst = ['hello', 'python', 'world']
print(res)                                              # hello python world

