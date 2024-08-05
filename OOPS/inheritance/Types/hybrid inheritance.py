# hybrid inheritance
# in hybrid inheritance we have multiple parent class and multiple child class. it means only one child has either multiple or single parent class.in simple word any child class has any parent class.

class School:
	def func1(self):
		print("This function is in school.")

class Student1(School):
	def func2(self):
		print("This function is in student 1. ")

class Student2(School):
	def func3(self):
		print("This function is in student 2.")

class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")

# Driver's code
object = Student3()
object.func1()      # This function is in school.
object.func2()      # This function is in student 1. 
