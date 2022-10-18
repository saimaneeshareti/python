'''
    5. Write a function to take a dict as argument. Return the key that has max value.
    Example : 
            testDict={10:20, 3:30, 4:16,90:100,20:31,11:23,17:44,20:400}
            result=func_exec(testDict)
            print(result)
            Expected Output : {20:400}
            Reason:
                400 is > 20
                400 is > 30
                400 is > 16
                400 is > 100
                400 is > 31
                400 is > 23
                400 is > 44

    Solution steps:
    **************
    From the original dict and iterate both key-value
        store values in _values
        checking for current key-value is greater than remaining 
        if Yes:
            add key-value to new dict
        else:
            continue loop
    Finally return new dict            
'''

#define funtion
def funDict(org_dict):
    #define new dict
    new_dict={}
    #stores values in a list
    _values=org_dict.values()
    #iterates keys and values simantanously from original dict
    for _key,_value in org_dict.items():
        #checking for current key-value is greater than reamaining key-values
        if(_value==max(_values)):
            #updating new_dictionary
            new_dict[_key]=_value
   #finally returns new dict
    return new_dict

# TestCase 1
testDict={10:20,3:30,4:16,90:100,20:31,11:23,17:44,20:400}
result=funDict(org_dict=testDict)
print("Final Result 1 :: {} ".format(result))
 
# TestCase 2
testDict={10:20,3:30,4:16,90:10,20:31,11:23,17:44,20:40}
result=funDict(org_dict=testDict)
print("Final Result 2 :: {} ".format(result))

# TestCase 3
testDict={1:2,13:3,24:6,9:45,56:98,67:84,78:95,89:40}
result=funDict(org_dict=testDict)
print("Final Result 3 :: {} ".format(result))

# TestCase 4
testDict={8:2,8:9,5:1,90:100,20:11,1:23,17:94,12:89}
result=funDict(org_dict=testDict)
print("Final Result 4 :: {} ".format(result))

# TestCase 5
testDict={78:87,5:8,9:19,60:7,8:23,12:78,18:56,10:40}
result=funDict(org_dict=testDict)
print("Final Result 5 :: {} ".format(result))

# TestCase 6
testDict={15:120,63:83,84:76,70:80,50:3,91:23,87:4,28:42}
result=funDict(org_dict=testDict)
print("Final Result 6 :: {} ".format(result))

# TestCase 7
testDict={10:6,93:90,74:86,80:50,70:81,51:25,18:4,50:40}
result=funDict(org_dict=testDict)
print("Final Result 7 :: {} ".format(result))

# TestCase 8
testDict={16:2,3:39,84:76,9:78,29:61,18:78,18:44,19:40}
result=funDict(org_dict=testDict)
print("Final Result 8 :: {} ".format(result))

# TestCase 9
testDict={79:20,83:30,67:15,60:17,29:31,11:23,17:44,20:40}
result=funDict(org_dict=testDict)
print("Final Result 9 :: {} ".format(result))

# TestCase 10
testDict={13:2,43:3,34:12,9:19,39:31,14:23,17:4,2:4}
result=funDict(org_dict=testDict)
print("Final Result 10 :: {} ".format(result))
