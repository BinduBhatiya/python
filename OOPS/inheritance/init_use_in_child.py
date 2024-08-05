# create simple inheritance in python.
class parent_class:
    def __init__(self,name):
        self.name = name
    def myfunc(self):
        print("my name is ",self.name)
class child_class(parent_class):
    def __init__(self,name):
        parent_class.__init__(self,name)

obj = child_class("krishna")
obj.myfunc()                # my name is  krishna


'''
    When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
'''