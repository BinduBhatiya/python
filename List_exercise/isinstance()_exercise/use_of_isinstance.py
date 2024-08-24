# SIMPLE USE OF ISINSTANCE() FUNCTION.

# EXERCISE 1:

x = 5
print(isinstance(x, int))                                   # True


# EXERCISE 2:

lst = [1,2,3,4,5]
print(isinstance(lst, (list,tuple)))                        # True


# EXERCISE 3:

class info:
    pass
obj = info()
print(isinstance(obj,info))                                 # True


# EXERCISE 4:

class parent:
    pass
class derived(parent):
    pass
obj = derived()
print(isinstance(obj,derived))                                 # True
print(isinstance(obj,parent))                                  # True