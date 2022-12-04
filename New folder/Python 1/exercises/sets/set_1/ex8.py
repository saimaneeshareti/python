'''From the list pick the elements that are not EVEN. Add those elements to new list. 
Finally print the new list.'''

l1=[24,65,89,90,60,4,2,9,11,15]
l2=[]
for i in l1:
  if(i % 2 != 0):
    l2.append(i)
print(l2)    