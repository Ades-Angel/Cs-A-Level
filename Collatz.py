import Terminal_clear
import time



def user_input():
  print('''This is a Collatz conjecture program, it will return the sequence and the number of times it looped through.
Enter a 0 to quit the program.''')
  time.sleep(4)
  while True:
    Terminal_clear.clear()
    number = int(input('Please enter a number: '))
    if number > 0:
      print()
      print("The Collatz sequence is:")
      recursion_collatz(number)
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
  print(1, end=' ')


user_input()
