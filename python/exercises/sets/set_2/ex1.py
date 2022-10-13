'''Write a function to take a list and a number X as arguments.
 From the list pick all numbers that are > er number X. Add those numbers to new list. Finally return the new list.
'''

def function_list(l1,x):
  l1 = list(l1)
  l2 = []
  x = int(x)
  for i in l1:
    if (i>x):
      l2.append(i)
  return l2
print(function_list([1,3,5,7,9,10],3))  
