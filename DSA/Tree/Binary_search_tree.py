# binary search tree

class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        print("ROOT---->",node)
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node

def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)
        print(root.data, end=' ')
        inOrderTraversal(root.right)

if __name__ == "__main__":
    
    root = None
    # Let's create the tree shown in the above figure
    # data_list = [25,20,5,7,10,15]
    data_list = [50,6,1,2,4,3]
    
    for data in data_list:
        root = insert(root, data)

    
    inOrderTraversal(root)
     
# output :
# 5,7,10,15,20,25

'''

                                15
                            ____|____
                            |        |
                            7        25
                        ____|____  ___|____
                        |        | |       
                        5       10 20                                                 
'''     
    

