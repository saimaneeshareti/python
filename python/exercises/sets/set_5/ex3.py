'''Write a function to take 2 lists. Use zip function to iterate the list and pick values that are common at both indexes.'''

def check_list(org_listA, org_listB):  

#define empty list
    new_mapper=[]
#iterates 2 list Simanatanously using the zip
    for listA_var, listB_var in zip(org_listA, org_listB):
#checking for both the elements from 2 lists are equal if condition true element adds to    new_mapper
            if(listA_var==listB_var):
#adding element to new list
                    new_mapper.append(listA_var)
#finally return the new list        
    return  new_mapper
    
# Execution
testListA=[100,20,300,40,50,60,100]
testListB=[1100,20,1300,40,50,160,1000]
#function calling
result=check_list(org_listA=testListA,org_listB=testListB)
#print result
print("Final Result is :: {} ".format(result))



