# single inheritance :
# in single inheritance we have one parent class and one child class. in which child class inherit from parent class.

class myclass1:
    def myfunc1():
        print('this is parent class.')
class myclass2(myclass1):
    def myfunc2():
        print('this is child class.')
obj = myclass2
obj.myfunc1()   # this is parent class.
obj.myfunc2()   # this is child class.
