# What is inheritance ?
'''
    inheritance is the process of creating a new class from of existing class it means 
    child classs inherit the property of parent class. 
'''


# create simple inheritance in python.
class parent_class:
    def __init__(self,name):
        self.name = name
    def myfunc(self):
        print("my name is ",self.name)
class child_class(parent_class):
    pass

obj = child_class("krishna")
obj.myfunc()                # my name is  krishna
