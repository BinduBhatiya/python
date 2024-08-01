class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

root = TreeNode(10)
node1 = TreeNode(20)
node2 = TreeNode(30)
node3 = TreeNode(40)
node4 = TreeNode(50)
node5 = TreeNode(60)
node6 = TreeNode(70)
node7 = TreeNode(80)

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node6.left = node7

inOrderTraversal(root)

# output :
# 40, 20, 50, 10, 60, 30, 80, 70,

'''

                                10
                            ____|____
                            |        |
                           20        30
                        ____|____  ___|____
                        |        | |       |
                       40       50 60      70
                                            |
                                           80

'''

