# HOW TO FIND THE LENGTH OF VALUES IN DICTIONARY.

# EXERCISE 1:-
# USING SIMPLE FOR LOOP :
dic = {1:'python', 2:'is', 3:'best'}
lst = {}
for val in dic.values():
    lst[val] = len(val)
print(lst)      # {'python': 6, 'is': 2, 'best': 4}



# EXERCISE 2:-
# USING DICTIONARY COMPREHENSION :
dic = {1:'python', 2:'is', 3:'best'}
res = str({val: len(val) for val in dic.values()})
print(res)      # {'python': 6, 'is': 2, 'best': 4}



# EXERCISE 3:-
# USING LAMBDA,MAP :
dic = {0:'python', 7:'is', 5:'best'}
res = dict(map(lambda val: (val[1], len(val[1])), dic.items()))
print(str(res))     # {'python': 6, 'is': 2, 'best': 4}


