# add properties in child class.

class parent:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def myfunc(self):
        print(self.firstname,self.lastname)
class child(parent):
    def __init__(self, fname, lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year 
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
obj = child('Bindu','Bhatiya',2024)
obj.welcome()


# output :
# Welcome Bindu Bhatiya to the class of 2024