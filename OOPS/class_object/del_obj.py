class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("Hello my age is " , self.age)

p1 = Person("John", 36)
p1.myfunc()
del p1
print(p1)

# output :
'''
    Hello my name is John
    Hello my age is  36
    
    NameError: name 'p1' is not defined
'''

# to show this output we can say python is interpreted programming language.

