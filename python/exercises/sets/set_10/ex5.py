'''
   5. Write a function to take a dict as an argument. 
	Find the key that has least value and return the key.

	Example : 
		testDict={1:4,10:100,3:90,4:40,6:80,12:200}
		result=func_exec(testDict)
		print(result)
		Expected Output : 1
		Reason: Output is 1 since 1 has value of 4 which is lesser than other values


	Example : 
		testDict={1:4,10:100,3:90,4:40,6:80,12:200,1000:3}
		result=func_exec(testDict)
		print(result)
		Expected Output : 1
		Reason: Output is 1000 since 1000 has value of 3 which is lesser than other values

    Solution Steps:
    **************
    Iterate the original dictionary
    Values are store in variable
    Find the minimum value from the variable
    Finally return the key
'''

def check_min(Org_dict):
    #store the values from original dict
    _values=Org_dict.values()
    #iterate keys and values from original dict
    for _key,_value in Org_dict.items():
    #check for current value is the minimum value from the original dict
        if(_value==min(_values)):
    #return key
            return _key


#Testcase 1
result=check_min({1:4,10:100,3:90,4:40,6:80,12:200})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 2
result=check_min({1:4,10:100,3:90,4:40,6:80,12:200,1000:3})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 3
result=check_min({32:3,42:5,75:3,83:80,63:75,60:23})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 4
result=check_min({5:125,410:10,45:31,72:73,520:310,53:31})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 5
result=check_min({300:50,4:3,500:80,9:5,9:2,12:17})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#TestCase 6
result=check_min({42:21,517:31,750:35,73:36,830:83,9:5})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 7
result=check_min({121:11,6:61,14:41,17:71,13:31,15:51})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 8
result=check_min({2:3,6:7,4:5,7:8,5:6,3:4})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 9
result=check_min({9:5,8:4,7:3,6:2,5:1,10:7})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 10
result=check_min({18:81,17:71,19:91,27:72,22:22,32:23})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
