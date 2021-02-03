my_list = [1,2,3,5,11,12,13,20,21,22,40,49,50]
number_to_find = 1 # Referred to as x in the functions


def linear_search(my_list, x):
  found = False
  n = len(my_list)
  for i in range(n):
    global position
    position = i 
    if my_list[i] == x:
      found = True
      break
  if found == True:
    print(x, 'was found at postion', i, 'in the list.')
  else:
    print(x, 'was not found in the list.')


def binary_search(my_list, x):
  n = len(my_list)
  start = 0
  end = n 
  found = False
  while (start <= end):
    global mid
    mid = (start + end) //2
    if x == my_list[mid]:
      found = True
      break
    if x < my_list[mid]:
      end = mid - 1
    else:
      start = mid + 1
  if found == True:
    print(x,'was found at postion', mid,'in the list.')
  else:
    print(x, 'was not found in the list.')



linear_search(my_list, number_to_find)
binary_search(my_list, number_to_find)