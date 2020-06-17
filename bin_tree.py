class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
class Bin_tree:
	def __init__(self):
		self.root = None
	
	def add(self, data):
		if self.root is None:
			self.root = Node(data)
		else(self._add(data, self.root)
		     
	def _add(self, data, node):
		if data <= node.data:
		     if node.left:
		     	self._add(deta, node.left)
		     else:
		     	node.left = Node(data)
		else:
		     if node.right:
		     	self._add(data, node.right)
		     else:
		     	node.right = Node(data)
		     
	def find_key(self, key):
		if self.root:
		     return self._find(key, self.root)
		else:
		     print('Tree is empty')
		     
	def _find(self, key, node):
		if key == node.data:
		     print('Find', key)
		elif key < node.data and node.left is not None:
		     self._find(key, node.left)
		elif key > node.data and node.right is not None:
		     self._find(key, node.right)
		else:
		     print('Given key not in tree')
		     
