import Terminal_clear
import time


def user_input():
  print('''This is a Fibonacci sequence calculator, it will give you the sequence.
Please enter a 0 to quit the program.''')
  time.sleep(5)
  while True:
    Terminal_clear.clear()
    number = int(input('Please enter a number: '))
    if number < 0:
      print('Please enter a positive number.')
      time.sleep(3)
    elif number == 0:
      break
    else:
      print('The Fibonacci sequence is: ')
      for i in range(number):
        print(recursion_fibonacci(i))
      time.sleep(3)


def recursion_fibonacci(number):
  if number <= 1:
    return number
  else:
    return recursion_fibonacci(number - 1) + recursion_fibonacci(number - 2)


user_input()
