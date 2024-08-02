# print the data using linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None 
    
data = [1, 2, 3, 4, 5]

for i in range(len(data)):
    current = Node(data[i])
    current.next = data[i]+1
    currentNode = current
    print(currentNode.data, end=" -> ")
print("none")
    






