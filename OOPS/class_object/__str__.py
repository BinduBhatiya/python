# use __str__ method:

class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name},{self.age}"
p1 = myclass("Lakhu","21")
print(p1)       # Lakhu,21