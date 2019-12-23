#Number of integers in a list that are divisible by 10.

def divisible_by_ten(nums):
  counter = 0
  for i in nums:
    if i % 10 == 0:
      counter = counter + 1
    else:
      counter = counter
  return counter
  

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Append string to each element of a list and create a new list

def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append('Hello, ' + name)
  return greetings
    

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


#Delete starting even numbers
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Exponents

def exponents(bases, powers):
  raised_list = []
  for b in bases:
    for p in powers:
      raised = b ** p
      raised_list.append(raised)
  return raised_list
  
  
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

#over 9000

def over_nine_thousand(lst):
  lst_sum = 0
  for i in lst:
    lst_sum += i
    if lst_sum > 9000:
      break
  return lst_sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))


#Max Num (without using max() method.)

def max_num(nums):
  maximum = nums[0]
  for i in nums:
    if i > maximum:
      maximum = i
    else:
      continue
  return maximum


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#Same Values - create new list of values that match.

def same_values(lst1, lst2):
  lst3 = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      lst3.append(i)
  return lst3


#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Reversed List
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))








