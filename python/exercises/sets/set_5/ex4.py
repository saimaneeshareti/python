'''
   Write a function to take a dict as argument. Sort the dict by keys and return the dict.
    Example : 
            testDict={1:4,10:20,3:4,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,3:4,4:7,12:9,20:3,60:11}
            :param org_dic: Original dictionary passed by the User
            :return: New dic with filtered values ONLY
    Solution Steps:
    **************
    Iterate the original dictionary
    Write condition for sort dictionary
    Add to new dictionary and return                  
'''

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

# Test case 1
testDict={1:4,10:20,3:4,4:7,60:11,12:9}
result=key_sort(org_dic=testDict)
print("Final Result 1 :: {} ".format(result))

# Test case 2
testDict={2:4,11:20,36:4,47:7,9:11,22:9}
result=key_sort(org_dic=testDict)
print("Final Result 2 :: {} ".format(result))

# Test case 3
testDict={1:42,10:24,3:24,4:71,60:15,12:91}
result=key_sort(org_dic=testDict)
print("Final Result 3 :: {} ".format(result))

# Test case 4
testDict={12:34,3:6,7:5,22:46,6:1,2:91}
result=key_sort(org_dic=testDict)
print("Final Result 4 :: {} ".format(result))

# Test case 5
testDict={8:4,1:20,3:34,4:6,6:1,2:9}
result=key_sort(org_dic=testDict)
print("Final Result 5 :: {} ".format(result))

# Test case 6
testDict={12:4,1:2,36:4,7:7,92:11,2:9}
result=key_sort(org_dic=testDict)
print("Final Result 6 :: {} ".format(result))

# Test case 7
testDict={2:14,11:2,36:43,47:73,9:1,22:29}
result=key_sort(org_dic=testDict)
print("Final Result 7 :: {} ".format(result))

# Test case 8
testDict={12:34,1:20,26:43,37:73,92:11,12:92}
result=key_sort(org_dic=testDict)
print("Final Result 8 :: {} ".format(result))

# Test case 9
testDict={21:43,15:24,32:44,42:71,92:15,25:19}
result=key_sort(org_dic=testDict)
print("Final Result 9 :: {} ".format(result))

# Test case 10
testDict={23:44,1:24,6:43,30:72,91:15,2:19}
result=key_sort(org_dic=testDict)
print("Final Result 10 :: {} ".format(result))
