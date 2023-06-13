#Defining a calss Node 
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

#Function to do an InOrderTraversal
def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.right) #Traversing the left Tree
        print(root.value, end = " ") #Printing the value at the nod3
        inOrderTraversal(root.left) #Traversing the right Tree

#Function to do an PreOrderTraversal
def preOrderTraversal(root):
    if root is not None:
        print(root.value, end = " ") #Printing the value at the nod3
        preOrderTraversal(root.left) #Traversing the left Tree
        preOrderTraversal(root.right) #Traversing the right Tree

#Function to do an PostOrderTraversal
def postOrdertraversal(root):
    if root is not None:
        postOrdertraversal(root.left) #Traversing the left Tree
        postOrdertraversal(root.right) #Traversing the right Tree
        print(root.value, end = " ")  #Printing the value at the nod3


#Building the Tree:
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

# Performing the traversals
print("In-order Traversal:")
inOrderTraversal(root)

print("\nPre-order Traversal:")
preOrderTraversal(root)

print("\nPost-order Traversal:")
postOrdertraversal(root)