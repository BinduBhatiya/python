# add properties in child class.

class parent:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def myfunc(self):
        print(self.firstname,self.lastname)
class child(parent):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        self.finalyear = year 
obj = child('Bindu','Bhatiya',2024)
obj.myfunc()
print("add new properties final year: ",obj.finalyear)    # 2024