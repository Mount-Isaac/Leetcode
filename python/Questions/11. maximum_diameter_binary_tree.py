'''
Given a binary tree, find its maximum diameter (or width). The diameter of a binary tree 
is defined as the length of the longest path between any two nodes in the tree. This path 
may or may not pass through the root of the tree. The length of a path is represented by 
the number of edges between the nodes.
'''

class BST:
	def __init__(self, key):
		self.root = None
		self.left = None
		self.right = None
		self.val = key

    #search a given element in a BST
	def search(self, root, key):
		if self.root is None or self.root.val == self.key:
			return self.root
		if self.root.val < self.key:
			return search(self.root.right, self.key)
		return search(self.root.left, self.key)

    #insert a new node 
	def insert(self, root, key):
		if self.root is None:
			return BST(self.key)
		else:
			if self.root.val == self.key:
				return self.root
			elif self.root.val < self.key:
				self.root.right = insert(self.root.right, self.key)
			else: 
				self.root.left = insert(self.root.left, self.key)
		return self.root

    #perform an inorder traversal
	def inorder(self, root):
		if self.root:
			inorder(self.root.left)
			print(self.root.val)
			inorder(self.root.right)




bst = BST(10)
bst.insert(10,8)