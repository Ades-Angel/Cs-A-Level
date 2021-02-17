import Terminal_clear
import time

class Node:

  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def insert(self, data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = Node(data)
        else:
          self.left.insert(data)
      elif data > self.data:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.insert(data)
      else:
        self.data = data

  def find_value(self, value):
    if value < self.data:
      if self.left is None:
        print(str(value)+" Not Found")
      else:
        return self.left.find_value(value)
    elif value > self.data:
      if self.right is None:
        print(str(value)+" Not Found")
      else:
        return self.right.find_value(value)
    else:
      print(str(self.data) + ' is found')

  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print( self.data)
    if self.right:
      self.right.PrintTree()


def user_input():
  print('This is a Binary Tree, please enter the root for your tree:')
  tree_root = input()
  root = Node(tree_root)
  Terminal_clear.clear()
  while True:
    Terminal_clear.clear()
    print('''What would you like to do to the Binary Tree:
Add
Search 
Delete # Not working for now
Exit ''')
    choice = input()
    operation_choice = choice.lower()
    Terminal_clear.clear()
    if operation_choice == 'add':
      print('What would you like to add to the tree: ')
      number = input()
      root.insert(number)
      Terminal_clear.clear()
      print('This is your Tree: ')
      print()
      root.PrintTree()
      time.sleep(3)
    elif operation_choice == 'search':
      print('What would you like to search: ')
      search_number = input()
      Terminal_clear.clear()
      root.find_value(search_number)
      time.sleep(3)
    elif operation_choice == 'exit':
      break


user_input()
