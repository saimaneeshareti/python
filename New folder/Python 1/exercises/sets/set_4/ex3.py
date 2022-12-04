'''Write a function to take a list as an argument. Find all the elements that occur in EVEN indexes & remove all duplicates.'''

def even_index(org_list):

#define new empty list
  new_mapper=[] 
#loop i value contains even numbers and step number is 2
  for i in range(0,len(org_list),2):
    
    new_mapper.append(org_list[i])
#finally returns new list  
  return new_mapper 

# Execution
testList=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
# function calling
result=even_index(org_list=testList)
# finally print the result
print("Final Result is :: {} ".format(result))