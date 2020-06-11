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
		if self.head is None:
			self.head = new_node
			return
		last_element = self.head
		while last_element.next:
			last_element = last_element_next
		last_element.next = new_node
			
	def delete_node(self, key):
		if key is None or self.head is None:
			return
		#check if head.data equals the key
		if self.head.data == key: #if true - delete head and new head - is a ex head next element
			self.head = self.head.next 
			return
		temp = self.head
		while temp is not None:
			if temp.data == key:
				break
			#else
			prev = temp
			temp = temp.next
		if temp == None:
			return
		#else
		prev.next = tepm.next
		temp = None
			prev = temp
