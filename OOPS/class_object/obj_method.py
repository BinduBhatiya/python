# create simple function.

class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(f"my name is '{self.name}'")      # my name is 'krishna'
p1 = myclass("krishna",21)
p1.myfunc()