from collections import deque
import os
import subprocess
import time


def clear():
  if os.name in ('nt','dos'):
    subprocess.call("cls")
  elif os.name in ('linux','osx','posix'):
    subprocess.call("clear")
  else:
    print("\n") * 120


queue = deque([' ', ' ', ' '])


def queue_choices():
  global size
  global set_max
  queue_limit = input('Would you like to have a limit to the queue? (yes or no):')
  if queue_limit == 'yes':
    size = int(input('Enter the size of the queue: '))
    set_max = True
  elif queue_limit == 'no':
    size = 9999
    print('Since you did not choose a limit, it was automatically set to 9999')
    set_max = False
  else:
    input('Invalid option please enter "yes" or "no".')


def select_operation():
  while True:
    choice = input(
'''Select which operation you would like to perform to the queue:
Add
Delete
Add vip
Exit 
Please enter an operation.
''')
    operation_choice = choice.lower()
    if operation_choice == 'add':
      enqueue()
    elif operation_choice == 'delete':
      dequeue()
    elif operation_choice == 'add vip':
      add_vip()
    elif operation_choice == 'exit':
      clear()
      break
    else:
      print('Invalid option, please enter the number of the operation.')
    clear()


def enqueue():
  clear()
  if set_max == True and size == len(queue):
    print('The queue is full.')
    time.sleep(3)
  else:
    item_to_add = input('What would you like to append to the queue:')
    queue.append(item_to_add)
    print(item_to_add, 'was added to the queue.')
    print(queue)
    time.sleep(3)
    clear()


def dequeue():
  clear()
  if not queue:
    print('Queue is empty')
    time.sleep(2)
  else:
    print(queue.popleft(), 'was removed from the queue.')
    print()
    print(queue)
    time.sleep(3)
  clear()


def add_vip():
  clear()
  vip_to_add = input('What vip would you like to add to the queue:')
  queue.appendleft(vip_to_add)
  print(vip_to_add, 'was added to the queue.')
  print(queue)
  time.sleep(5)
  clear()


queue_choices()
select_operation()
