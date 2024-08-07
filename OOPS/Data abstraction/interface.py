# intrface :
'''
    interface is similar to abstract class because if we can use only abstract method in class then it is called "interface" otherwise if we can use abstract method and normal method in class then it is called "abstract method".

    Note :
    1. we can not create object of interface.
    2. we use interface when an action is common but implementation.
    3. all child class should be inherits abstract method.

    syntax :

    import abc
    class interface_class(ABC):
        @abstractmethod
        def show1()
            pass

        @abstractmethod
        def show2()
            pass   
'''
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def show(self):
        pass
class square(shape):
    def show(self):
        print("square has 4 sides.")
class triangle(shape):
    def show(self):
        print("triangle has 3 sides.")

s = square()
s.show()            # square has 4 sides.

t = triangle()
t.show()            # triangle has 3 sides.

