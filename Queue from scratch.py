class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class Queue:

  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self, data):
    if self.tail == None:
      self.head = Node(data)
      self.tail = self.head
    else:
      self.tail.next = Node(data)
      self.tail.next.prev = self.tail
      self.tail = self.tail.next

  def dequeue(self):
    if self.head == None:
      return None
    else:
      temp = self.head.data
      self.head = self.head.next
      self.head.prev = None
      return temp
  
  def first_element(self):
    return self.head.data
  
  def size(self):
    temp = self.head
    count = 0
    while temp == None:
      count = count + 1
      temp = temp.next
    return count
  
  def is_empty(self):
    if self.head == None:
      return True
    else:
      return False

  def print_queue(self):
    print('The elements in the queue are: ')
    temp = self.head
    while temp != None:
      print(temp.data, end='->')
      temp = temp.next

if __name__ == '__main__':
  queue = Queue()
  print('Queue operations using double linked list')
  queue.enqueue(4) 
  queue.enqueue(5) 
  queue.enqueue(6) 
  queue.enqueue(7) 
  queue.print_queue() 
   
  print("\nfirst element is ",queue.first_element())
  print("Size of the queue is ",queue.size()) 
   
  queue.dequeue() 
  queue.dequeue() 
   
  print("After applying dequeue() two times") 
  queue.print_queue() 
   
  print("\nqueue is empty:",queue.is_empty()) 
