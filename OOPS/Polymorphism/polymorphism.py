# polymorphism :
# polymorphism "poly" means "multiple" and "morphism" means "forms". it means ability to take multiple form.
# it is devided in two way.
# 1. method overloading   2. method overriding

class myclass1:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
    def move(self):
        print("hello")
class myclass2:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
    def move(self):
        print("python")
class myclass3:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
    def move(self):
        print("world")

obj1 = myclass1("cat","meow")
obj2 = myclass2("dog","huskey")
obj3 = myclass3("cow","Gir")

for x in (obj1, obj2, obj3):
    print("data of ",x.__class__.__name__," :")
    x.move()
    print(x.brand)
    print(x.model)


# output :
'''
    data of  myclass1  :
    hello
    cat
    meow
    data of  myclass2  :
    python
    dog
    huskey
    data of  myclass3  :
    world
    cow
    Gir
'''