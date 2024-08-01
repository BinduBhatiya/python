class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 
def preData(node):
    if node is None:
        return
    preData(node.left)
    preData(node.right)
    print(node.data, end=', ')
    
root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

preData(root)


# output :
# C, D, A, E, G, F, B, R, 