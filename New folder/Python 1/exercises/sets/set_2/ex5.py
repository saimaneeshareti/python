'''Write a function to take a list as an argument. If the element is even then multiply that element by 100, if the element is odd then 
multiply that element by 200. Finally return the new list.'''

def number_list(l1,x):
  l1 = list(l1)
  l2 = []
  x = int(x)
  for i in l1:
    if(i%2==0):
      l2.append(i*100)
    else:
      l2.append(i*200)
  return l2
print(number_list([1,3,5,7,9,10,12,15,20,25],3))