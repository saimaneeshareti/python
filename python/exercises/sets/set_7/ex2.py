'''
    Write a function to take a list, number Y as arguments.
    Filter all the numbers from the EVEN indexes, divisible by number Y. Remove duplicates.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        numY=10
        result=func_exec(listA,numY)
        print(result)
        Expected Output : [30,50,100]
    Example :
        listA=[10,21,301,41,501,50,1100,11,12,13]
        numY=10
        result=func_exec(listA,numY)
        print(result)
        Expected Output : [1100]
    Example :
        listA=[10,20,30,40,50,60,100,11,120,13,100]
        numY=10
        result=func_exec(listA,numY)
        print(result)
        Expected Output : [30,50,100,120]

    :param list: List passed by the User
    :param numY: Number Y passed by the User.
    :return: Even indexes divisible by number Y, without duplicates  

  Solution Steps :
  ****************
    Iterate the original list
    From the list pic the EVEN indexes
    From the EVEN indexes check the number is divisible by number Y:
    Check if the number divisible by numberY, and number not present in new list      
        if yes:
          number add to new list
        else:
          continue loop    
    finally return new list      
'''

def check_eve_ind(org_list,numy):
  #define new list
  new_list=[]
  #loop produce odd numbers from 1 to size of the original
  for i in range(0,len(org_list),2):    
    #checking for number is even
    if(org_list[i]%numy==0):
      #checking for number is not present in new list
      if(org_list[i] not in new_list):
        #addiing number to new list
        new_list.append(org_list[i])
  #finally reterns new list
  return new_list

# Test case 1
testorg_list=[10,20,30,40,50,60,100,11,12,13]
numy=10
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))    

# Test case 2
testorg_list=[10,21,301,41,501,50,1100,11,12,13]
numy=20
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))    

# Test case 3
testorg_list=[10,20,30,40,50,60,100,11,120,13,100]
numy=15
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))    

# Test case 4
testorg_list=[28,39,20,18,39,40,50,19,20]
numy=20
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))    

# Test case 5
testorg_list=[13,30,29,18,27,39,48,50,20,18]
numy=25
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))

# Test case 6
testorg_list=[39,48,10,38,48,59,19,3]
numy=25
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))

# Test case 7
testorg_list=[14,37,19,28,39,49,50,48,20]
numy=30
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))

# Test case 8
testorg_list=[2,40,39,50,10,39,40,59,59]
numy=35
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))

# Test case 9
testorg_list=[40,38,20,18,29,40,48,59,27]
numy=33
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))

# Test case 10
testorg_list=[30,20,48,19,39,49,57,61,39]
numy=36
result=check_eve_ind(org_list=testorg_list,numy=numy)
print("Final Result is :: {} ".format(result))