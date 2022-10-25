'''
   Write a function to take a dict as argument. 
	If the dict-val is the divisible bydict-key then filter, add to new dict.
   Finally return the new dict.

	Example : 
			testDict={10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400}
			result=func_exec(testDict)
			print(result)
			Expected Output : {10:20,3:30,4:16,20:400}
			Reason: 
				20 is divisible by 10
				30 is divisible by 3
				16 is divisible by 4
				400 is divisible by 20

    Solution Steps:
    **************
    Iterate Original dictionary from keys and values
    Check if condition in  dict-val is the divisible by dict-key 
    If Yes:
    add to new dictionary
    else:
    continue loop
    Finally return the new dictionary                          
'''
def check_div (org_dic):
    # Define the empty dictionary
    new_dic={}
    # Iterate the dictionary key(i) and value(j) 
    for i,j in org_dic.items():
        # Check the condition for dict-val is the divisible by dict-key  
        if (j%i==0):
            # update the new dictionary
            new_dic[i]=j
    # Finally return the new dictionary        
    return new_dic

#Testcase 1
result=check_div({10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 2
result=check_div({22:44,5:3,33:11,4:8,9:4,77:22})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 3
result=check_div({32:3,42:5,75:3,83:13,63:75,61:23})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 4
result=check_div({3:2,40:10,45:31,72:73,52:31,55:30})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 5
result=check_div({3:5,4:3,5:8,9:5,9:2,12:17})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#TestCase 6
result=check_div({42:21,57:31,75:31,73:36,83:31,9:12})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 7
result=check_div({12:21,16:61,14:41,17:34,13:31,68:51})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 8
result=check_div({21:42,6:7,4:5,7:8,5:6,3:4})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 9
result=check_div({9:5,8:4,7:3,6:2,5:1,10:7})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 10
result=check_div({180:810,17:71,19:91,270:720,22:22,32:23})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
        