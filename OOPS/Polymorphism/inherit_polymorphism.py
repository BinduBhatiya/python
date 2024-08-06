# inherit polymorphism :
class myclass1:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("python")
class child1(myclass1):
    def move(self):
        print("hello")
class child2(myclass1):
    pass
class child3(myclass1):
    def move(self):
        print("world")
obj1 = child1("dog","huskey") 
obj2 = child2("cat","meow")
obj3 = child3("cow","Gir")

for x in (obj1,obj2,obj3):
    print("data of ",x.__class__.__name__)
    x.move()
    print(x.brand)
    print(x.model)


# output :
'''
    data of  child1
    hello
    dog
    huskey
    data of  child2
    python
    cat
    meow
    data of  child3
    world
    cow
    Gir
'''