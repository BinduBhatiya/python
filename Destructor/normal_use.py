# what is Destructor ?
'''
    in simple word destructor is used for delete object. because, we can perform multiple program and create multiple
object. these object can take multiple space. so, we need to maintain the space of memory. so we used destructor which
will help to remove object and maintain space.

here, it is not required to define both item like "del obj" & "__del__" function. if we use only one even though it is 
remove object.

'''

# normal use of destructor.

class myclass:
    def __init__(self):
        print("this is constructor method.")
    def show(self):
        print("it is normal method.")
    def __del__(self):
        print("this is destructor method.")
obj = myclass()
obj.show()

del obj     # delete object.
# obj.show()    # if we want to check the object is deleted or not then we can call function one more time. if object is delete then it will raise error. otherwise print the statement. 


# output :
'''
    this is constructor method.
    it is normal method.
    this is destructor method.
'''