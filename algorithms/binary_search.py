# https://www.youtube.com/watch?v=PnnsDf3zEMw

""" Big O - Simplified analysis of an algorithm's efficiency
		- worst-case
		- best-case
		- average-case 
"""

"""  Recursion:
	Hint: use helper_methods
	Optimize by using instead iterative functions: queues and stacks
"""

""" Strings
	- How to iterate over each character
	- Palindromes and Anagrams
"""

""" Hash Maps
"""

""" Linear Data Structures
	- Array
	- Linked List
	- Queues
	- Stacks
"""

"""
tree traversal
	preorder
	inorder 
	postorder
	breath first search
	depth breath search
binary search

data structures to represent a tree

recursion limited by stack space
recursive algorithim
stacks and queues instead of recursion
hashmap
object oriented for structure

dynamic programming -> memoization

time and memory 
"""

------------------------------------------------------------------------

""" linear search """

def linear_search(data: list, target: int) -> bool:
	for i in range(len(data)):
		if data[i] == target:
			return True
	return


""" Iterative binary search
	
Time complexity: O(log n) - 1 billion entries = 30 operations 
							to find the target
"""
def binary_search_iterative(data: list, target:int) -> bool:

	""" Split the given list into halfs. Then validate 
		if the target is egual, lower or greater 
		than the mid point value
	"""

	low = 0
	high = len(data) - 1

	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False

""" Tree Traversal 

Depth First Traversals: 
	(a) Inorder (Left, Root, Right) : 4 2 5 1 3 
	(b) Preorder (Root, Left, Right) : 1 2 4 5 3 
	(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Breadth-First or Level Order Traversal: 1 2 3 4 5

"""

class Node:
    def __init__(self, val):
        self.__left = None
        self.__right = None
        self.__val = val

def inorder_traversal(root):
	if root is not None:
		inorder_traversal(root.left)
		print(root.data)
		inorder_traversal(root.right)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node3 = Node(4)
node3 = Node(5)
node3 = Node(6)
node3 = Node(7)
node3 = Node(8)
node3 = Node(0)

------------------------------------------------------------------------

""" Sort Algos
	- Bubble Sort
	- Merge Sort
	- Quick Sort
"""

""" Bubble Sort
for i from 1 to N
	for j from 0 to N - 1
		if a[j] > a[j+1]
			swap(a[j], a[j+1])
"""