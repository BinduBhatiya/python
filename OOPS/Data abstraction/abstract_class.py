# abstract class is a class that contains one or more abstract method is called abstract class.
# Note :
'''
    1. an object of an abstract class cannot be created.
    2. python provide abc module to work with abstraction.
    3. we use @abstractmethod decorator to define abstract method. 
'''

from abc import ABC, abstractmethod
class car(ABC):
    def show(self):
        print("every car has four wheel.")
    @abstractmethod
    def speed(self):
        pass
class Thar(car):
    def speed(self):
        print('speed of ',__class__.__name__,' is 100km/1H.')
class BMW(car):
    def speed(self):
        print('speed of ',__class__.__name__,' is 150km/1H.')
obj1 = Thar()
obj1.show()     # every car has four wheel.
obj1.speed()    # speed of  Thar  is 100km/1H.

obj2 = BMW()
obj2.show()     # every car has four wheel.
obj2.speed()    # speed of  BMW  is 150km/1H.

# output :
'''
    every car has four wheel.
    speed of  Thar  is 100km/1H.
    every car has four wheel.
    speed of  BMW  is 150km/1H.
'''
