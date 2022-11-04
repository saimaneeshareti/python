'''
    Write a function to take a dict as argument. Find the key that has max value.
	Example : 
			testDict={1:4,10:20,3:40,4:7,60:11,12:9}
			result=func_exec(testDict)
			print(result)
			Expected Output : {3:40}
			Reason: Key "3" has value of "40" >er than other values
            :param org_dict: Original dictionary passed by the User
            :return: New dictionary with filtered values ONLY.      
                
    Solution steps:
    **************
    Take original dict and iterate key-value simantanously
        store values in variable
        checking for current value is greater then stored varible values
        if Yes:
            add key-value to new dict
        else:
            continue loop
    Finally return new dict
'''
# Define function
def check_num(dic): 
    new_dic={}
    # Store the dictionary values in variable
    val=dic.values()
    # Iterate the dic   
    for _key,_value in dic.items():        
        # Find the max value from dictionary
        if (_value==max(val)):
            # Update the new dict
            new_dic[_key]=_value
    # Finally return  the key        
    return new_dic

# Function calling          
print(check_num({1:4,10:20,3:40,4:7,60:11,12:9}))            