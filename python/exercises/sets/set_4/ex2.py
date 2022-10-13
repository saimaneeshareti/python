'''Write a function to take a list as an argument. Find all the elements that occur in ODD indexes.'''

def odd_index(org_list):

#define an empty new list
  new_mapper=[] 
# loop i value contains odd numbers
  for i in range(1,len(org_list),2): 
#elements adds to new list from original list which are in odd indexs
    new_mapper.append(org_list[i]) 
#finally return the new list with odd indexes elements 
  return new_mapper  

# Execution
testList=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
#function calling
result=odd_index(org_list=testList)
#finally print result
print("Final Result is :: {} ".format(result))
