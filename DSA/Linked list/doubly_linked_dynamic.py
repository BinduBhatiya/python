class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 
    
data = [1, 2, 3, 4, 5]

for i in range(len(data)):
    current = Node(data[i])
    current.next = data[i]+1
    #current.prev = data[i]-1
    currentNode = current
    print(currentNode.data, end=" -> ")
print("none")

n = len(data)-1
for i in range(n,-1,-1):
    current = Node(data[i])
    #current.next = data[i]+1
    current.prev = data[i]-1
    currentNode = current
    print(currentNode.data, end=" -> ")
print("none")
    