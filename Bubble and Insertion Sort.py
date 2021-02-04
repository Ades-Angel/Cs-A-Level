''' 
mark first element as sorted

for each unsorted element X

  'extract' the element X

  for j = lastSortedIndex down to 0

    if current element j > X

      move sorted element to the right by 1

    break loop and insert X here
'''
import random
import time 


def generate_Numbers():
    randomList = []
    for i in range(0,10):
        randomNumbers = random.randint(1,50)
        randomList.append(randomNumbers)
    print(randomList)
    return randomList


def bubble_sort(our_list):
    n = len(our_list)
    for i in range(n):
        for j in range(n-1):
            if our_list[j] > our_list[j+1]:
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                print(our_list)


def insertion_sort(our_list):
  n = len(our_list)
  for i in range(n):
    
    


our_list = generate_Numbers()
b_start = time.time()
bubble_sort(our_list)
b_end = time.time()
b_elapsed = b_end - b_start
formatted_time = "{:.4f}".format(b_elapsed)
print(formatted_time)

