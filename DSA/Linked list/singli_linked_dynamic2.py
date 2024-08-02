# print the data using linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None 
    
data = [1, 2, 3, 4, 5]
    
head = Node(data[0])
current = head

for value in data[1:]:
    new_node = Node(value)
    current.next = new_node
    current = new_node

current_node = head 
while current_node:
    print(current_node.data,'->',end=' ')
    current_node = current_node.next
print(None)


# 3 -> 5 -> 4 -> 11 -> None
