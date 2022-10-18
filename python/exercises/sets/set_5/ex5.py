'''
   Write a function to take a dict as argument. Sort the dict by values and return the dict.
    Example : 
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,4:7,12:9,60:11,10:20,3:40}
            :param org_dic: Original dictionary passed by the User
            :return: New dic with filtered values ONLY
   Solution Steps:
   **************
   Iterate the original dictionary
   Write condition for sort dictionary values
   Add to new dictionary and return                  
'''

def sort_value(org_dic):
    #define empty dictionary
    new_mapper={}
    #values() method gives list of values
    #stores sorted list of values
    _val=sorted(org_dic.values()) 
    #iterates values one by one
    for _key in _val:    
        #iterates keys from original dict one by one
        for _val in org_dic: 
            #checking for values and keys if condition true it adds to new dict. 
            if(_key==org_dic[_val]):   
                #add key-value pair to new dictionary
                new_mapper[_val]=_key  
    # finally return the new dic                         
    return new_mapper               

# Test case 1
testDict={1:4,10:20,3:40,4:7,60:11,12:9}
result=sort_value(org_dic=testDict)
print("Final Result 1 :: {} ".format(result))

# Test case 2
testDict={1:34,10:2,3:4,4:27,60:1,12:29}
result=sort_value(org_dic=testDict)
print("Final Result 2 :: {} ".format(result))

# Test case 3
testDict={12:4,11:20,23:40,54:7,6:11,12:9}
result=sort_value(org_dic=testDict)
print("Final Result 3 :: {} ".format(result))

# Test case 4
testDict={3:9,1:2,4:6,5:2,6:13,1:9}
result=sort_value(org_dic=testDict)
print("Final Result 4 :: {} ".format(result))

# Test case 5
testDict={1:3,10:9,3:2,4:17,6:13,1:91}
result=sort_value(org_dic=testDict)
print("Final Result 5 :: {} ".format(result))

# Test case 6
testDict={12:14,11:19,3:4,34:71,63:1,1:4}
result=sort_value(org_dic=testDict)
print("Final Result 6 :: {} ".format(result))

# Test case 7
testDict={12:14,1:4,3:4,5:7,6:1,2:9}
result=sort_value(org_dic=testDict)
print("Final Result 7 :: {} ".format(result))

# Test case 8
testDict={12:14,1:20,13:4,54:17,16:11,12:19}
result=sort_value(org_dic=testDict)
print("Final Result 8 :: {} ".format(result))

# Test case 9
testDict={2:14,21:20,23:30,54:71,6:41,12:91}
result=sort_value(org_dic=testDict)
print("Final Result 9 :: {} ".format(result))

# Test case 10
testDict={12:56,11:10,23:50,54:74,6:1,12:95}
result=sort_value(org_dic=testDict)
print("Final Result 10 :: {} ".format(result))
