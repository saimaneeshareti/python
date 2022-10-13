'''Write a function to take a list as an argument. Remove all duplicates from the list. Don't use any built-in. Check using if conditions.'''


def remove_dupl(org_list):

#define an empty new list
    new_mapper=[] 
# itarate the list
    for i in org_list: 
#checking for an element is in an empty list, if an element is present it ignored as a duplicate
        if (i not in new_mapper): 
#elements add to new list
            new_mapper.append(i) 
#finally returns a new list without duplicates        
    return new_mapper 
    

# Execution
test_list=[1,2,3,4,5,6,7,8,9,10,11,12,1,1,2,4,4,5,6,7]
result=remove_dupl(org_list=test_list)
print("Final Result is :: {} ".format(result))