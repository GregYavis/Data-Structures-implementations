class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class Linked_list:
	def __init__(self):
		self.head = None
		
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
			
	def insert_aft_key(self, key, new_data):
			new_node = Node(data)
			temp = self.head
			while temp.next:
				temp = temp.next
				if temp.data == key:
					new_node.next = temp.next
					temp.next = new_node
					break
					
	def insert_aft_node(self, prev_node, new_data):
		if prev_node is None:
			return ('Given node doesnt exist in this linked list)
		else:
			new_node = Node(new_data)
			new_node.next = prev_node.next
			prev_node.next = new_node
	
	def append_to_end(self, new_data):
			new_node = Node(new_data)
