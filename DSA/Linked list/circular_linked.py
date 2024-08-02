# circular linked list :

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
node1 = Node(2)
node2 = Node(4)
node3 = Node(6)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

current_node = node1 
present = node1
print(current_node.data,'->',end=' ')       # 2 ->
current_node = current_node.next

while current_node != present:
    print(current_node.data,'->',end=' ')   # 4 -> 6 -> 8 -> ....inf....
    current_node = current_node.next
print('....inf....')


# output :
# 2 -> 4 -> 6 -> 8 -> ....inf....

