import random
import time


def generate_list():
  global my_list
  print("How many numbers would you like to generate and sort? (integers only)")
  n = int(input())
  print()
  print("Enter the minimum and maximum of the randomly generated numbers")
  range_min = int(input("Min: "))
  range_max = int(input("Max: "))
  my_list = []
  for i in range(n):
    random_int = random.randint(range_min, range_max)
    my_list.append(random_int)
  return my_list 



def bubble_sort(our_list):
    n = len(our_list)
    noswaps = True
    while noswaps == True:
        for i in range(n-1):
            noswaps = False
            if our_list[i] > our_list[i+1]:
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                noswaps = True
                print(our_list)
        n = n - 1
    print(our_list)



def insertion_sort(our_list):
    print(our_list)
    for index in range(1, len(our_list)):
        current_value = our_list[index]
        current_position = index
        while current_position > 0 and our_list[current_position - 1] > current_value:
            our_list[current_position] = our_list[current_position - 1]
            current_position = current_position - 1
            our_list[current_position] = current_value


def time_to_sort():
  generate_list()
  start_time_bubble = time.time_ns()
  bubble_sort(my_list)
  finish_time_bubble = time.time_ns()
  time_taken_bubble = (finish_time_bubble - start_time_bubble)
  print('It took Bubble sort',time_taken_bubble, 'ns to sort the list.')

  start_time_insertion = time.time_ns()
  insertion_sort(my_list)
  finish_time_insertion = time.time_ns()
  time_taken_insertion = (finish_time_insertion - start_time_insertion)
  print('It took Insertion sort',time_taken_insertion, 'ns to sort the list.')


time_to_sort()
