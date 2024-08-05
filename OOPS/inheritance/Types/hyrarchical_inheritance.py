# hyrarchical inheritance
# in hyrarchical inheritance we have only one parent class and multiple child class. it is opposite operation of multiple inheritance.

class my_class1:
    def myfunc1(self):
        print("it is parent class.")
class my_class2(my_class1):
    def myfunc2(self):
        print("it is one child class.") 
class my_class3(my_class1):
    def myfunc3(self):
        print("it is second child class.")  

obj1 = my_class2()
obj2 = my_class3()

obj1.myfunc1()  # it is parent class.
obj1.myfunc2()  # it is one child class.

obj2.myfunc1()  # it is parent class.
obj2.myfunc3()  # it is second child class.







