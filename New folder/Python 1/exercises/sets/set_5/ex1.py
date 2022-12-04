'''Write a function to take a list. Reverse and return the new list.'''

def reverse_list(org_list):

# define empty list
  new_mapper = [] 
# itearate the orginal list
  for i in reversed(org_list): 
# add elements in to new list
    new_mapper.append(i) 
# finally return the new list
  return new_mapper 

# Execution
testList=[10,20,30,40,50,60,100]
#function calling
result=reverse_list(org_list=testList)
# print the result
print("Final Result is :: {} ".format(result))
 


