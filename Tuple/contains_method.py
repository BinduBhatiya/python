
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


# MEMBERSHIP OPERATOR ('in', 'not in')

list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
set1 = {1, 2, 3, 4, 5}
dict1 = {1: "DSU", 2:"Bindu", 3:"10000"}
tup1 = (1, 2, 3, 4, 5)

print(2 not in list1)                           # False 
print('O' not in str1)                          # True
print(6 not in set1)                            # True
print(3 not in dict1)                           # False
print(9 not in tup1)                            # True
