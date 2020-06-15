class Stack_node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class Stack:
  def __init__(self):
    self.root = None
    
  def is_empty(self):
    return self.root is None
    
  def push(self, data):
    new_node = Stack_node(data)
    new_node.next = self.root
    self.root = new_node
    print("%d pushed" %data)
    
  def pop(self):
    if self.is_empty():
      return float('inf)
    temp = self.root
    self.root = self.root next
    poped_element = temp.data
    print("%d poped" %poped_element)
    return poped_element
    
  def peek(self):
    if self.is_empty():
      return float('inf')
    return self.root.data
    
  def print_stack(self):
    if self.is_empty():
      print('Stack is empty')
      return
    content = []
    temp = self.root
    while temp:
      content.append(temp.data)
      temp = temp.next
    print(content)
