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

#del obj 


# output :
'''
    this is constructor method.
    it is normal method.
    this is destructor method.
'''