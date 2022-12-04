'''Define a list of 10 elements.From the list pick all numbers that are > er 100. Add those numbers to new list.
 Finally print the new list.'''

l1=[15,20,30,115,120,80,580,310,40,50]
l2=[]
for i in l1:
  if(i>100):
    l2.append(i)
print(l2)    