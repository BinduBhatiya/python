# HOW TO SORT NESTED LIST.

# EX 1:
# data = ['splender','ola',['ather','dio']]
# print(data.sort())

# TypeError: '<' not supported between instances of 'list' and 'str'

# EX 2:
data = [['apple','google'], ['zest','scooty'], ['amazon','google','yahoo']]
data.sort()
print(data)                 # [['amazon', 'google', 'yahoo'], ['apple', 'google'], ['zest', 'scooty']]



# EX 3:
nested_list = [[3, 'a'], [1, 'b'], [2, 'c']]
sorted_list = sorted(nested_list)
print(sorted_list)         # [[1, 'b'], [2, 'c'], [3, 'a']]


# EX 4:
nested_list = [[3, 'a'], [1, 'c'], [2, 'b']]
sorted_list = sorted(nested_list, key = nested_list[1])
print('--->',sorted_list)         # [[3, 'a'], [2, 'b'], [1, 'c']]


# EX 5:
nested_list = [[3, 'a'], [1, 'b'], [2, 'c']]
nested_list.sort()
print(nested_list)         # [[1, 'b'], [2, 'c'], [3, 'a']]

# EX 6:
nested_list = [[3, 'a'], [1, 'c'], [2, 'b']]
nested_list.sort(key=lambda x: x[1])
print(nested_list)          # [[3, 'a'], [2, 'b'], [1, 'c']]

# EX 7:
data = [['apple','google'], ['zest','scooty'], ['amazon','google','yahoo']]
data.sort(reverse=True)
print(data)                 # [['zest', 'scooty'], ['apple', 'google'], ['amazon', 'google', 'yahoo']]

# EX 8:
data = ['splender','ola','ather','dio']
data.sort(key=len)
print(data)                 # ['ola', 'dio', 'ather', 'splender']

