import os
import subprocess
import time


def clear():
  if os.name in ('nt','dos'):
    subprocess.call("cls")
  elif os.name in ('linux','osx','posix'):
    subprocess.call("clear")
  else:
    print("\n") * 12


def user_input():
  print('''This is a Collatz conjecture program, it will return the sequence and the number of times it looped through.
Enter a 0 to quit the program.''')
  time.sleep(4)
  while True:
    clear()
    number = int(input('Please enter a number: '))
    if number > 0:
      print()
      print("The Collatz sequence is:")
      print(recursion_collatz(number))
      print('The count is:', count)
      time.sleep(6)
    elif number == 0:
      break
    else:
      print('Please enter a postive integer.')
      time.sleep(2)
    


def recursion_collatz(number):
  global count 
  count = 0
  while number > 1:
    print(number, end=' ')
    if number % 2 :
      number = 3*number + 1
      count = count + 1
    else:
      number = number//2
      count = count + 1
  print(1)


user_input()
