'''
    Write a function to take a list. Sort and return the new list.
    Example :
        listA=[100,20,300,40,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : [20,40,50,60,100,100,300]
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY
    Solution Steps:
    **************
    Iterate the original list
     Write condition for sort list
     Add to new list and return          
'''   

def sort(org_list):

    #define new list
    new_mapper=[]
    # sort the orginal list as listA
    for i in sorted(org_list):
        #adds to new list
        new_mapper.append(i)
    #Finally return new sorted list           
    return new_mapper
    
# Test case 1 
testList=[100,20,300,40,50,60,100]
result=sort(org_list=testList)
print("Final Result 1 :: {} ".format(result))

# Test case 2 
testList=[20,30,10,50,69,55,63,29]
result=sort(org_list=testList)
print("Final Result 2 :: {} ".format(result))

# Test case 3 
testList=[79,55,43,52,62,79,64,25,11]
result=sort(org_list=testList)
print("Final Result 3 :: {} ".format(result))

# Test case 4 
testList=[10,190,34,100,59,30,28,93,10]
result=sort(org_list=testList)
print("Final Result 4 :: {} ".format(result))

# Test case 5 
testList=[125,20,36,16,25,93,29]
result=sort(org_list=testList)
print("Final Result 5 :: {} ".format(result))

# Test case 6 
testList=[89,11,20,35,63,190,20,48]
result=sort(org_list=testList)
print("Final Result 6 :: {} ".format(result))

# Test case 7
testList=[93,20,4,2,58,190,27,389,28]
result=sort(org_list=testList)
print("Final Result 7 :: {} ".format(result))

# Test case 8 
testList=[93,10,28,39,47,89,26,1,39,20]
result=sort(org_list=testList)
print("Final Result 8 :: {} ".format(result))

# Test case 9 
testList=[19,24,38,39,47,59,10,40,46,20]
result=sort(org_list=testList)
print("Final Result 9 :: {} ".format(result))

# Test case 10 
testList=[19,25,40,58,20,59,60,2,48]
result=sort(org_list=testList)
print("Final Result 10 :: {} ".format(result))


