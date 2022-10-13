'''Write a function to take a list, number X as arguments. From the list pick the elements that are not divisible by number X.
 Add those elements to new list. Finally return the new list.'''

def number_list(l1,x):
  l1 = list(l1)
  l2 = []
  x = int(x)
  for i in l1:
    if(i%x!=0):
      l2.append(i)
  return l2
print(number_list([1,3,5,7,9,10],3))   