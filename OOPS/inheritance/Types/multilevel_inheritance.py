# multilevel inheritance 
# in multilevel inheritance we have multiple parent class and multiple child class it means child class is the parent class of another child class.

class Grandfather:
    def __init__(self,grandfather_nm):
        self.grandfather_nm = grandfather_nm

class Father(Grandfather):
    def __init__(self,father_nm,grandfather_nm):
        self.father_nm = father_nm
        Grandfather.__init__(self, grandfather_nm)

class Son(Father):
    def __init__(self, son_nm, father_nm, grandfather_nm):
        self.son_nm = son_nm

        Father.__init__(self, father_nm, grandfather_nm)

    def print1(self):
        print("Grand Father is: ",self.grandfather_nm)
        print("Father is: ",self.father_nm)
        print("Son is: ",self.son_nm)

obj = Son("Lav-Kush", "Ram", "Dasharath")
print(obj.grandfather_nm)
obj.print1()


# output :
'''
    Dasharath
    Grand Father is:  Dasharath
    Father is:  Ram
    Son is:  Lav-Kush
'''



