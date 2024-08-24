# Encapsulation :
# python provides access to all the variable and method globally. By using Encapsulation, we can restrict the variable and method access globally by making it private or protected. 
# 1. single underscore (protected) _a
# 2. double underscore (private) __b

class myclass:
    _a = 10     # protected
    __b = 20    # private
    def show(self):
        print("a = ",self._a)       # a =  10
        print("b = ",self.__b)      # b =  20
obj = myclass()
obj.show()
print(obj._a)       # 10
# print(obj.__b)      # AttributeError: 'myclass' object has no attribute '__b'


