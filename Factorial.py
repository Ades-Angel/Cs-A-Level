import Terminal_clear
import time


def user_input():
  global number
  print('This is a factorial calculator, it will calculate the factorial for your number')
  print()
  time.sleep(4)
  while True:
    Terminal_clear.clear()
    number = int(input('Please enter a number: '))
    if number < 0:
      print('Factorial only works for psotive number')
      time.sleep(2)
    elif number == 0:
      print('The factorial of 0 is 1')
      time.sleep(2)
    else: 
      print('The factorial of', number, 'is', recursion_factorial(number))
      time.sleep(3)


def  recursion_factorial(number):
  if number == 1:
    return 1
  else:
    return number*recursion_factorial(number - 1) 

user_input()
