class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        """Print the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    
    # Create the linked list
    ll = LinkedList()
    
    # Create the head node
    ll.head = Node(data[0])
    
    # Keep track of the current node
    current = ll.head
    
    # Iterate over the remaining data and create nodes
    for value in data[1:]:
        new_node = Node(value)
        current.next = new_node
        current = new_node
    
    # Print the linked list
    ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
