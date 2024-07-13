# basic example in which create class and object.

class student:
    def putdata(self):
        self.id = int(input("enter the id : "))
        self.stu_name = input("enter the name : ")
    def display(self):
        print("student id : ",self.id)
        print("student name : ",self.stu_name)
obj = student()
obj.putdata()
obj.display()

# output :
'''
enter the id : 10
enter the name : krishna
student id :  10
student name :  krishna
'''

# if we use  "__init__"  method then we does not require to call the method.

'''

class student:
    def __init__(self):
        self.id = int(input("enter the id : "))
        self.stu_name = input("enter the name : ")
    def display(self):
        print("student id : ",self.id)
        print("student name : ",self.stu_name)
obj = student()
obj.display()

'''

