''' Write a function to take a list. Sort and return the new list.'''

def sort(org_list):

    #define new list
    new_mapper=[]
    # sort the orginal list as listA
    for i in sorted(org_list):
        #adds to new list
        new_mapper.append(i)
    #Finally return new sorted list           
    return new_mapper
    
# Execution
testList=[100,20,300,40,50,60,100]
#Calling function
result=sort(org_list=testList)
#output final result
print("Final Result is :: {} ".format(result))


