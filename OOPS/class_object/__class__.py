# simple use of __class__ method.

class myclass:
    attr1 = "mummal"
    def __init__(self,name):
        self.name = name 
    def myfunc(self):
        print("dog name is ",self.name)

# create object        
dog1 = myclass("husky") 
dog2 = myclass("tommy")

# fetch value of class attribute using __class__
print('dog1 is ',dog1.__class__.attr1)          # we can also pass dog1.attr1 
print('dog2 is also a ',dog2.__class__.attr1)

# call the function
dog1.myfunc()
dog2.myfunc()

# output :
'''
    dog1 is mummal
    dog2 is also a mummal

    dog name is husky
    dog name is tommy
'''
