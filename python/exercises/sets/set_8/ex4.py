'''
   4. Write a function to take a dict as argument. If the dict-val is the divisible bydict-key then filter, add to new dict.
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
    Take a dict and iterate both keys and values
    check for value is divisible by key
    if Yes:
      add key and value to new dict
    else
      continue loop
    Finally return new dict             
                
'''

#define function
def check_div(org_dict):
    #deine new dict
    new_dict={}
    #iterates keys and values simantanously
    for _key,_value in org_dict.items():
      #checking for is value is divisible by key
      if(_value%_key==0):
        #add key and value to new dict
        new_dict[_key]=_value
    #finally return new dict    
    return new_dict

# TestCase 1
x=check_div({10:15,3:30,4:16,90:100,20:30,11:23,17:44,20:400})
print('final output 1 : {}'.format(x))

# TestCase 2
x=check_div({10:2,10:30,5:15,1:30,10:30,11:2,7:4,2:40})
print('final output 2 : {}'.format(x))

# TestCase 3
x=check_div({1:5,4:30,2:10,9:10,2:3,2:34,7:6,2:4})
print('final output 3 : {}'.format(x))

# TestCase 4
x=check_div({10:5,3:5,2:16,5:10,18:3,1:20,14:7,4:6})
print('final output 4 : {}'.format(x))

# TestCase 5
x=check_div({10:3,2:10,10:5,9:10,2:8,11:10,1:9,2:5})
print('final output 5 : {}'.format(x))

# TestCase 6
x=check_div({18:3,3:15,10:40,9:27,12:4,1:4,13:9,12:45})
print('final output 6 : {}'.format(x))

# TestCase 7
x=check_div({19:5,2:13,14:59,12:98,15:10,13:9,22:45})
print('final output 7 : {}'.format(x))

# TestCase 8
x=check_div({10:8,12:10,10:45,19:15,12:48,15:16,15:39,22:54})
print('final output 8 : {}'.format(x))

# TestCase 9
x=check_div({10:43,52:16,13:25,19:11,32:84,14:16,19:89,12:65})
print('final output 9 : {}'.format(x))

# TestCase 10
x=check_div({10:53,12:16,14:25,39:19,92:58,13:10,18:9,12:5})
print('final output 10 : {}'.format(x))