# doubly_linked list :

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
node1 = Node(3)
node2 = Node(5)
node3 = Node(7)
node4 = Node(9)

node1.prev = None
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = None

current_node = node1
while current_node:
    print(current_node.data,'->',end=' ')   # 3 -> 5 -> 7 -> 9 -> None
    current_node = current_node.next
print(None)


current_node = node4
while current_node:
    print(current_node.data,'->',end=' ')   # 9 -> 7 -> 5 -> 3 -> None
    current_node = current_node.prev
print(None)


# output :
# 3 -> 5 -> 7 -> 9 -> None
# 9 -> 7 -> 5 -> 3 -> None