# multiple inheritance :
# in multiple inheritance we have multiple parent class and one child class. it means one child class inherit multiple parent class.
# method 1 :

class myclass1:
    def myfunc1():
        print('this is parent class.')
class myclass2:
    def myfunc2():
        print('this is second parent class.')
class myclass3(myclass2,myclass1):
    def myfunc3():
        print('this is child class.')
obj = myclass3
obj.myfunc1()
obj.myfunc2()
obj.myfunc3()

# output :
'''
    this is parent class.
    this is second parent class.
    this is child class.
'''


# method 2 :
class Mother:
    mother_nm = ""
    def mother(self):
        print(self.mother_nm)
class Father:
    father_nm = ""
    def father(self):
        print(self.father_nm)
class Son(Mother,Father):
    def son(self):
        print("father : ",self.father_nm)
        print("mother : ",self.mother_nm)
obj = Son()
obj.father_nm = "vasudev"
obj.mother_nm = "devkiji"
obj.son()
# obj.father()
# obj.mother()


# output :
'''
    father :  vasudev
    mother :  devkiji
'''