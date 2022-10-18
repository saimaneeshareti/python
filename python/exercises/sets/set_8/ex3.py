'''
    3. Write a function to take a dict as argument. If the dict-key and dict-val are both PRIME then filter, add to new dict.
    Finally return the new dict.
    Example : 
            testDict={10:20, 3:30, 4:40,90:100,20:30,11:23,17:44}
            result=func_exec(testDict)
            print(result)
            Expected Output : {11:23}

    Solution Steps:
    ****************
    Take a dict and iterate both keys and values        
    check for co-factors if found any co-factors between these range loop will break
        if yes:
           loop will break
        else:
           add the new dictionary
    Finally return new dict 
'''
 
def check_prime(org_dict):
        #define new dict
        new_dict={}        
        #itrates keys and values simantanously
        for _key,_value in org_dict.items():
                #loop for checking key is prime
                for i in range(2,_key):
                        #checking for co-factors if found any co-factors between these range loop will break
                        if(_key%i==0 or _key<2):
                          break
                else:
                        #checking for value is prime
                        for j in range(2,_value):
                                #if found any co-factors between these range loop will break
                                if(_value%j==0 or _value<2):
                                         break   
                        else:
                                #both key and value prime,so add to new dictionary
                                 new_dict[_key]=_value     
         #finally return new dictionary               
        return new_dict      

#Testcase 1
result=check_prime({10:20, 3:30, 4:40,90:100,20:30,11:23,17:44})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 2
result=check_prime({2:7,5:3,3:1,4:8,9:4,7:2})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 3
result=check_prime({32:3,42:5,75:3,83:80,63:75,60:23})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 4
result=check_prime({3:2,4:1,45:31,72:73,52:31,53:31})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 5
result=check_prime({3:5,4:3,5:8,9:5,9:2,12:17})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#TestCase 6
result=check_prime({42:21,57:31,75:31,73:36,83:31,9:5})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 7
result=check_prime({12:21,16:61,14:41,17:71,13:31,15:51})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 8
result=check_prime({2:3,6:7,4:5,7:8,5:6,3:4})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 9
result=check_prime({9:5,8:4,7:3,6:2,5:1,10:7})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 10
result=check_prime({18:81,17:71,19:91,27:72,22:22,32:23})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
       

