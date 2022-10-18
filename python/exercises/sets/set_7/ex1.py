'''
    Write a function to take a list. Filter all the even numbers from the ODD indexes. Remove duplicates.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : [20,40,60]
    Example :
        listA=[10,21,30,41,50,50,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : [50]
        
    :param listA: List passed by the User
    :return: Even Elements from ODD indexes without duplicates

    Solution Steps :
    ****************
    Iterate the original list
    From the list pic the ODD indexes
    From the ODD indexes check the number is even  
    check for number already not present in new list
      if number even:       
          number add to new list
      else:
        continue loop        
    Finally return new list

 '''

def check_eve_ind(org_list):

  #define new list
  new_list=[]
  #loop produce odd numbers from 1 to size of the original
  for i in range(1,len(org_list),2):    
    #checking for number is even
    if(org_list[i]%2==0):
      #checking for number is not present in new list
      if(org_list[i] not in new_list):
        #addiing number to new list
        new_list.append(org_list[i])
  #finally reterns new list
  return new_list

# Test case 1
testorg_list=[10,20,30,40,50,60,100,11,12,13]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

# Test case 2
testorg_list=[10,21,30,41,50,50,100,11,12,13]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

# Test case 3
testorg_list=[11,64,87,90,54,84,11,75,84,92]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

# Test case 4
testorg_list=[85,90,41,64,92,21,84,94,32,76]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

# Test case 5
testorg_list=[98,74,32,90,53,19,76,97,64]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

# Test case 6
testorg_list=[76,84,96,34,21,64,86,76,95]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

# Test case 7
testorg_list=[9,53,24,95,223,87,59,87]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

# Test case 8
testorg_list=[9,98,75,47,87,54,75,90,76,54]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

# Test case 9
testorg_list=[67,87,95,23,12,86,43,25]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

# Test case 10
testorg_list=[97.65,47,24,98,56,3,67,12,89]
result=check_eve_ind(org_list=testorg_list)
print("Final Result is :: {} ".format(result))

