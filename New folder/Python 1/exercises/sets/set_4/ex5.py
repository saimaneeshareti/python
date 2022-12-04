'''Write a function to take a dict and number X arguments. If the dict key is NOT divisible by number X, then
   add the key to new dict and finally return the new dict.'''

def check_not_div(org_dic,numx):
#difine an empty dictionary
    new_mapper={} 
    
#items method gives list of tuples from dictionary
# iterates keys and values from original dictionary
    for _key,_value in org_dic.items():
#checking for is key not divisible with value numx , if condition true the key and value is added to the new dictionary
        if (_key%numx!=0):
#adding key-value pair to new dictionary
            new_mapper[_key]=_value
#finally returns new dictionary        
    return new_mapper 
    

# Execution
testDict={1:4,10:20,3:4,4:7,60:11,12:9}
numx=10
#function calling
result=check_not_div(org_dic=testDict,numx=numx)
#finally print the result
print("Final Result is :: {} ".format(result))
