'''
    Write a function to take a dict as argument. Sort the dict by keys and return the dict.

	Example : 
			testDict={1:4,10:20,3:4,4:7,60:11,12:9}
			result=func_exec(testDict)
			print(result)
			Expected Output : {1:4,3:4,4:7,12:9,20:3,60:11}
'''

# Iterate the original dict
def key_sort(dic):
    # define new dic
    new_dic={}
    # iterate and sort original dict dict
    for k in sorted(dic):
        # Update new dic
        new_dic[k]=dic[k]
    # Finally return new dict    
    return new_dic

# Function calling
print(key_sort({1:4,10:20,3:4,4:7,60:11,12:9}))