'''
    Write a function to take a dict as argument. Sort the dict by values and return the dict.

	Example : 
			testDict={1:4,10:20,3:40,4:7,60:11,12:9}
			result=func_exec(testDict)
			print(result)
			Expected Output : {1:4,4:7,12:9,60:11,10:20,3:40}
'''
# Define function
def check_num(dic): 
    new_dic={}
    # Iterate the dic   
    for k,v in dic.items():
        # Store the dictionary values in variable
        val=dic.values()
        # Find the max value from dictionary
        if (v==max(val)):
            # Update the new dict
            new_dic[k]=v
    # Finally return  the key        
    return new_dic

# Function calling          
print(check_num({1:4,10:20,3:40,4:7,60:11,12:9})) 