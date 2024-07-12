# append()
# This method appends items to the end of the existing list.

colors = ["red","white","blue"]
colors.append("pink")
print(colors)                                                   # ['red', 'white', 'blue', 'pink']

# insert()
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

colors1 = ["red","white","blue"]
colors1.insert(1,"pink")
print(colors1)                                                  # ['red', 'pink', 'white', 'blue']

# extend()
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

bird = ["dove","peacock","parrot"]
animal = ["lion","cat","tiger","cow"]
bird.extend(animal)
print(bird)                                                     # ['dove', 'peacock', 'parrot', 'lion', 'cat', 'tiger', 'cow']

# concate two list

lst1 = ["1","2","3"]
lst2 = ["4","5","6"]
print(lst1 + lst2)                                              # ['1', '2', '3', '4', '5', '6']

# pop()
# This method removes the last item of the list if no index is provided. If an index is provided, then it removes item at that specified index.

flower = ["rose","merigold","champa"]
flower.pop()                                                    # ['rose,merigold']
flower.pop(0)                                                   # ['merigold']
print(flower)

# remove()
# This method removes specific item from the list.

color1 = ["red","white","blue"]
color1.remove("red")
print(color1)                                                   # ['white', 'blue']

# del()
# del is not a method, rather it is a keyword which deletes item at specific from the list, or deletes the list entirely.

color2 = ["red","white","blue"]
del color2[1]
print(color2)                                                   # ['red', 'blue']   

# clear()
# This method clears all items in the list and prints an empty list.

colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)                                                   # []

# sort()
# this method sort the list in ascending order.

cars = ["BMW","jaguar","THAR","mercedes","bugatti","Tesla"] 
cars.sort()
print(cars)                                                     # ['BMW', 'THAR', 'Tesla', 'bugatti', 'jaguar', 'mercedes']

# if you want print the data in descending order.

cars = ["BMW","jaguar","THAR","mercedes","bugatti","Tesla"] 
cars.sort(reverse=1)
print(cars)                                                     # ['mercedes', 'jaguar', 'bugatti', 'Tesla', 'THAR', 'BMW']

# reverse()
# this method is use to print reverse the data.

cars = ["BMW","jaguar","THAR","mercedes","bugatti","Tesla"] 
cars.reverse()
print(cars)                                                     # ['Tesla', 'bugatti', 'mercedes', 'THAR', 'jaguar', 'BMW']

# index()
# this method returns the index of the first occurence of the list item.

num = [7,9,3,4,1,5,0,3,5,1]
print(num.index(3))                                             # 2

# copy()
# it is used to copy the list.

num = [1,2,3,4,5]
cp = num.copy()
print("original list: ",num)                                    # original list:  [1, 2, 3, 4, 5]
print("copied list: ",cp)                                       # copied list:  [1, 2, 3, 4, 5]




# change List item :
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie"
print(names)                                                    # ['Harry', 'Sarah', 'Millie', 'Oleg', 'Steve']

# you can also change more than a single item.
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:4] = ["juan", "Anastasia"]
print(names)                                                    # ['Harry', 'Sarah', 'juan', 'Anastasia', 'Steve']

names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:3] = ["juan", "Anastasia", "Bruno", "Olga", "Rosa"]
print(names)                                                    # ['Harry', 'Sarah', 'juan', 'Anastasia', 'Bruno', 'Olga', 'Rosa', 'Oleg', 'Steve']




# list comprehension :
# accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)