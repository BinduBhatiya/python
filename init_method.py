# __init__ method example with argument.

class student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def average(self):
        return sum(self.marks)/len(self.marks)
    
obj = student(1,'krishna',[50,60,70,80,90])
print(obj.name)
print(obj.average())

# output :
'''
    krishna
    70.0
        '''
