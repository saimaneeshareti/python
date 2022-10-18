'''
   Write a function to take 2 lists. Use zip function to iterate the list and pick values that
   are common at both indexes.
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        result=func_exec(listA,listB)
        print(result)
        # 20 -> listA[1] == listB[1]
        # 40 -> listA[3] == listB[3]
        # 50 -> listA[4] == listB[4]
        Expected Output : [20,40,50]
        :param org_list: Original list(org_listA, org_listB) passed by the User
        :return: New list with filtered values ONLY
    Solution Steps:
    **************
    Iterate the original two lists using zip
    Write condition for comman values in list
    Add to new list and return              
'''   

def check_list(org_listA, org_listB):  
#define empty list
    new_mapper=[]
#iterates 2 list Simanatanously using the zip
    for listA_var, listB_var in zip(org_listA, org_listB):
#checking for both the elements from 2 lists are equal if condition true element adds to new mapper
            if(listA_var==listB_var):
#adding element to new list
                    new_mapper.append(listA_var)
#finally return the new list        
    return  new_mapper
    
# Test case 1
testListA=[100,20,300,40,50,60,100]
testListB=[1100,20,1300,40,50,160,1000]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 1 :: {} ".format(result))

# Test case 2
testListA=[100,50,40,67,84,96,58]
testListB=[50,78,96,40,58,84,100]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 2 :: {} ".format(result))

# Test case 3
testListA=[10,80,95,75,69,37,54,78]
testListB=[89,54,69,75,37,78,95,23]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 3 :: {} ".format(result))

# Test case 4
testListA=[50,43,75,80,96,74,85,53,29]
testListB=[67,75,96,53,29,50,43,74,85]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 4 :: {} ".format(result))

# Test case 5
testListA=[97,54,73,92,76,53,21,80,10]
testListB=[73,53,31,10,85,97,73,21,30]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 5 :: {} ".format(result))

# Test case 6
testListA=[64,80,52,75,31,97,32,91]
testListB=[87,92,80,31,97,80,32,76]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 6 :: {} ".format(result))

# Test case 7
testListA=[45,134,89,54,164,53,76,91]
testListB=[134,91,89,53,164,35,87,94]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 7 :: {} ".format(result))

# Test case 8
testListA=[65,97,53,87,13,64,75,90,43,10]
testListB=[53,75,89,54,90,43,76,16,97,43]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 8 :: {} ".format(result))

# Test case 9
testListA=[67,95,45,78,43,21,56,19,31,75]
testListB=[56,93,67,13,21,54,67,38,23,54]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 9 :: {} ".format(result))

# Test case 10
testListA=[75,95,89,64,90,43,85,92,64,87]
testListB=[64,87,95,90,64,65,87,32,20,43]
result=check_list(org_listA=testListA,org_listB=testListB)
print("Final Result 10 :: {} ".format(result))







