'''
    Write a function to take a list. From the list find the number that occurs most number of times.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : []
    Example :
        listA=[10,21,30,41,50,500,100,11,12,13,21]
        result=func_exec(listA)
        print(result)
        Expected Output : [21,]
    Example :
        listA=[10,21,30,41,50,50,100,11,12,13,21]
        result=func_exec(listA)
        print(result)
        Expected Output : [21,50]
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY.  
    Solution Steps:
    **************
    Iterate the orginal list 
    Check condition for most repeated element in the list and remove the duplicate numbers
      If yes:
        add the new list
      else:
        continue the loop  
    Add finally retun the new list
'''

def check_max(org_list):
  #define new empty list 
  new_list=[]  
  #iterates original list on by one  
  for i in org_list:
    #checking for number not present in new list    
    if(i not in new_list):
      #checking fo number than occurs repeatedly      
      if(org_list.count(i)>1):
        #ads number to new list
        new_list.append(i)
  #finally returns new list        
  return new_list

# Test case 1
testorg_list=[10,20,30,40,50,60,100,11,12,13]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result))    

# Test case 2
testorg_list=[10,21,30,41,50,500,100,11,12,13,21]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result))    

# Test case 3
testorg_list=[10,21,30,41,50,50,100,11,12,13,21]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result))    

# Test case 4
testorg_list=[20,38,39,47,10,20,38,34,10]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result))    

# Test case 5
testorg_list=[30,10,27,39,48,39,10,28,39]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result))    

# Test case 6
testorg_list=[39,10,29,37,46,53,29,39]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result))    

# Test case 7
testorg_list=[48,20,30,57,200,18,28,209]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result))    

# Test case 8
testorg_list=[20,19,20,38,49,109,20,98]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result)) 

# Test case 9
testorg_list=[10,38,29,30,49,57,10,29,20]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result))    

# Test case 10
testorg_list=[50,29,39,40,58,20,40,29,10]
result=check_max(org_list=testorg_list)
print("Final Result is :: {} ".format(result))    