class Queue:
  def __init__(self, capacity):
    self.front = self.size = 0
    self.end = capacity - 1
    self.Q = [None]*capacity
    self.capacity = capacity
  
  def q_is_full(self):
    return self.size == self.capacity
  
  def q_is_empty(self):
    return self.size == 0
    
  def add_to_q(self, data):# добавляем в конец очереди
    if self.q_is_full():
      print("Q if full")
      return 
    self.end = (self.end+1) % self.capacity
    # calculate index to push
    # element in position even if there was element in there before
    # deleting element in there
    self.Q[self.end] = data
    self.size = self.size + 1
    print('% added to queue' %str(data))
    
  def del_from_q(self):
    if self.q_is_empty():
      print("Queue is empty")
      return
    print("elemett %s dequed from queue" % self.Q[self.fromt])
    self.front = (self.front+1) % self.capacity
    self.size = self.size - 1
    
  def get_front(self):
    if self.q_is_empty():
      print("Queue is empty")
      return
    print('Front element is', self.Q[self.front])
    
  def get_end(self):
    if self.q_is_empty():
      print("Queue is empty")
      return
    print('Last element is', self.Q[self.end])
    
  def print_content(self):
    print(self.Q)
    
    
