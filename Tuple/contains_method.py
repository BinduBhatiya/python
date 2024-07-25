
# import module
import operator
print(operator.contains([1, 2, 3, 4, 5], 2))                    # True
print(operator.contains("Hello World", 'O'))                    # True
print(operator.contains({1, 2, 3, 4, 5}, 6))                    # False 
print(operator.contains({1: "Geeks", 2:"for", 3:"geeks"}, 3))   # True
print(operator.contains((1, 2, 3, 4, 5), 9))                    # False


# IDENTITY OPERATOR ('is', 'is not')
num1 = 5
num2 = 5

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst2 = lst1

str1 = "hello world"
str2 = "hello world"

# using 'is' identity operator on different datatypes
print(num1 is num2)     # True
print(lst1 is lst2)     # True
print(str1 is str2)     # True
print(str1 is str2)     # True
