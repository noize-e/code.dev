"""
Binary Tree

A binary tree is a tree data strcuture in which 
each node has at most 2 children which are referred 
to as the left and right child

     2
    / \\
   7   5
  / \\  \\
 2   6   9
"""
from enum import Enum


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Traversal(Enum):
    PREORDER = "preorder"
    INORDER = "inorder"
    POSTORDER = "postorder"


class BinaryTree(object):

    """ BinaryTree object class """

    def __init__(self, root: Node):
        self.root = root

    def traversal(self, traversal_order=Traversal.PREORDER):
        try:
            nodes_values = getattr(self, traversal_order.value)(self.root)
            return ','.join(nodes_values)
        except Exception as e:
            return e

    def preorder(self, start:Node, traversal:list=[]) -> list:
        if start:
            traversal.append(str(start.value))
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start:Node, traversal:list=[]) -> list:
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal.append(f"{start.value}")
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start:Node, traversal:list=[]) -> list:
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal.append(f"{start.value}")
        return traversal



binary_tree = BinaryTree(Node(1))
binary_tree.root.left = Node(2)
binary_tree.root.right = Node(3)
binary_tree.root.right.left = Node(4)
binary_tree.root.right.right = Node(5)

print(binary_tree.traversal())
print(binary_tree.traversal(Traversal.INORDER))
print(binary_tree.traversal(Traversal.POSTORDER))