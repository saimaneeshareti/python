'''
   Define a list of 10 elements.From the list pick all numbers that are > er 100. Add those numbers to new list.Finally print the new list.
'''

org_list=[15,20,30,115,120,80,580,310,40,50]
# Define new list
new_list=[]
# Iterate the list
for i in org_list:
  # Check condition, If number greater than 100  
  if(i>100):
    # Add to new list
    new_list.append(i)
# Finally print the new list    
print(new_list)    