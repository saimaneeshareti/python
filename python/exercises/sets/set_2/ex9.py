'''Write a function to take a list, number X,Y as arguments. From the list pick the elements that are >er than (X+Y). 
Add those elements to new list. Finally return the new list.'''

def num_list(l1,x,y):
  l1=list(l1)
  l2=[]
  x=int(x)
  y=int(y)
  for i in l1:
    if(i>(x+y)):
      l2.append(i)
  return l2
print(num_list([4,7,8,9,3],3,5))
