class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
    
  class Doubly_list:
    def __init__(self):
      self.head = None
      
    def push(self, data):
      new_node = Node(data)
      new_node.next = self.head
      new_node.prev = None
      if self.head is not None:
        self.head.prev = new_node
      self.head = new_node
      
    def append(self, data): #add to end
      new_node = Node(data)
      new_node.next = None
      if self.head is None:
        new_node.prev = None
        self.head = new_node
        return
      #start iterate
      last = self.head
      while last.next:
        last = last.next
      last.next = new_node
      new_node.prev = last
      
    def insert_after(self, prev, data):
      if prev is None:
        print('Node cannot be None')
        return
      new_node = Node(data)
      new_node.next = prev.next
      prev.next = new_node
      new_node.prev = prev
      if new_node.next is not None:
        new_node.next.prev = new.node
        
    def delete_key(self, key):
      current = self.head
      while current:
        if self.head.next is None:
          print('List have only one element')
          return
        if self.head.data == key:
          self.head = self.head.next
        if current.data == key:
          if current.next:
            current.next.prev = current.prev
          if current.prev:
            current.prev.next = current.next
        current = current.next
      return
        
    def print_DLList(self):
      if not self.head:
        print('List is empty')
      else:
        nodes_data = []
        node = self.head
        while node:
          nodes_data.append(node.data)
          node = node.next
        print(nodes_data)
