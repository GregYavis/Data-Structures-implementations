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
		     
	def clear_tree(self):
		self.root = None
	
	def sort(self):
		nodes = self._sort(self.root)
		self.clear_tree()
		for node in nodes:
		     self.add(node)
		return
		     
	def _sort(self, node):
		if node.left:
		     node.left = self._sort(node.left)
		else:
		     node.left = []
		if node.right:
		     node.right = self._sort(node.right)
		else:
		     node.right = []
		return node.left + [node.data] + node.right
	
	def print_levels(self, root):
		queue = []
		def bfs(node, lvl):
		     if node is None:
		     	return
		     if lvl >= len(queue):
		     	queue.append([node.data])
		     else:
		     	queue[lvl].append([node.data])
		     lvl += 1
		     bfs(node.left, lvl)
		     bfs(node.right, lvl)
		bfs(root, lvl)
		print(queue)
		     
	def inorder_print(self, root):
		if root:
		     self.inorder_print(root.left):
		     print(root.data)
		     self.inorder_print(root.right)
		     
	def postorder_print(self, root):
		if root:
		     self.postorder_print(root.left)
		     self.postorder.print(root.right)
		     print(root.data)
		     
	def preorder_print(self, root):
		if root:
		     print(root.data)
		     self.preorder_print(root.left)
		     self.preorder_print(root.right)
