'''Write a function to take a dict as an argument. Find the key that has maximum value and return the key.'''

def maximum_key(org_dic):

#store list of values from org_dictionary
    val=org_dic.values()    
#items method gives list of tuples from org_dictionary
# key and values iterates Simanatanously
    for _key,_value in org_dic.items():           
#checking for largest value in the org_dictionary, if condition true it returns the key for that large value
           if (max(val)==_value):
#finally returns the key of large value pair
              return _key             

# Execution
test_Dict={1:4,10:100,3:90,4:40,6:80,12:200}
result=maximum_key(org_dic=test_Dict,)
print("Final Result is :: {} ".format(result))