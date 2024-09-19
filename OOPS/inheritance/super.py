# create simple inheritance in python.
class parent_class:
    def __init__(self,name):
        self.name = name
    def myfunc(self):
        print("my name is ",self.name)
class child_class(parent_class):
    def __init__(self,name):
        super().__init__(name)  # here, we must not pass self keyword in argument. otherwise it throw error.

obj = child_class("krishna")
obj.myfunc()                # my name is  krishna


'''

    Python also has a super() function that will make the child class inherit all the methods and properties from its parent.
    by using super() we do not require to pass the name of parent class.
'''