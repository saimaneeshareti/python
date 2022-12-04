'''Write a function to take a dict as argument. Sort the dict by keys and return the dict.'''

def key_sort(org_dic):

    #define empty dictionary
    new_mapper={}    
    #sorted method on dictionary gives a list with sorted keys
    #iterates keys from least to maximum
    for i in sorted(org_dic):
        #adds key-value pair to new dictionary
        new_mapper[i]=org_dic[i]
    #finally return the new dic    
    return new_mapper


# Execution
testDict={1:4,10:20,3:4,4:7,60:11,12:9}
#function calling
result=key_sort(orgDictsort=testDict)
#finally print result
print("Final Result is :: {} ".format(result))