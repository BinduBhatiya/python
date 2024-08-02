class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
data = [1, 2, 3, 4, 5]
n = len(data)
i = 0
# while i < n:
#     current = Node(data[i])
#     if data[i] == data[n-1]:
#         current.next = data[0]
#     else:
#         current.next = data[i+1]
#     currentNode = current
#     print(currentNode.data, end=" -> ")
#     i = i+1
# print("...inf...")



# current = Node(data[i])
# if data[i] == data[n-1]:
#     current.next = data[0]
# else:
#     current.next = data[i+1]
# currentNode = current
# print(currentNode.data, end=" -> ")








# current_node = node1 
# present = node1
# print(current_node.data,'->',end=' ')       # 2 ->
# current_node = current_node.next

# while current_node != present:
#     print(current_node.data,'->',end=' ')   # 4 -> 6 -> 8 -> ....inf....
#     current_node = current_node.next
# print('....inf....')