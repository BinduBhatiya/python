# CHECK FOR THE VALUE IN LIST OR NOT USING "any()"

# EXRCISE 1 :
lst = [1,2,3,4,5]
res = any(lst)
print(res)           # True



# EXRCISE 2 :
lst = []
print(any(lst))        # False



# EXRCISE 3 :
lst = [' ', 'hello', 'world']
print(any(lst))           # True



# EXRCISE 4 :
lst = [1,2,3,4,5]
print(any(n > 5 for n in lst))         # False