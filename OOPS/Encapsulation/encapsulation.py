# Encapsulation :
# python provides access to all the variable and method globally. By using Encapsulation, we can restrict the variable and method access globally by making it private or protected. 
# 1. single underscore (protected) _a
# 2. double underscore (private) __b

class myclass:
    _a = 10     # protected
    __b = 20    # private
    def show(self):
        print("a = ",self._a) 
        print("b = ",self.__b)  
obj = myclass()
obj.show()
print(obj._a)


