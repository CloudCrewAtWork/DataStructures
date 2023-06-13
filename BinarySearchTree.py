class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inOrderTraversal(root):
    if root != None:
        inOrderTraversal(root.left)
        print(root.value, end = " ")
        inOrderTraversal(root.right)


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

