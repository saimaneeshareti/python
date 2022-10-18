'''
    Write a function to take a list. Reverse and return the new list.
    Example :
        listA=[10,20,30,40,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : [100,60,50,40,30,20,10]
        :param org_list: Original list passed by the User
        :return: return new list with org_list arg

    Solution Steps:
    **************
    Iterate the original list
    Write condition for reverse list
    Add to new list and return         
'''

def reverse_list(org_list):
# define empty list
  new_mapper = [] 
# itearate the orginal list
  for i in reversed(org_list): 
# add elements in to new list
    new_mapper.append(i) 
# finally return the new list
  return new_mapper 

# Test case 1
testList=[10,20,30,40,50,60,100]
result=reverse_list(org_list=testList)
print("Final Result 1 :: {} ".format(result))
 
# Test case 2
testList=[1,2,3,4,5,6,7,8,9,10]
result=reverse_list(org_list=testList)
print("Final Result 2 :: {} ".format(result))

# Test case 1
testList=[89,52,32,46,79,25,60]
result=reverse_list(org_list=testList)
print("Final Result 3 :: {} ".format(result))

# Test case 4
testList=[66,75,844,93,89,32,11,15]
result=reverse_list(org_list=testList)
print("Final Result 4 :: {} ".format(result))

# Test case 5
testList=[100,99,98,97,96,95,94,93,92,91]
result=reverse_list(org_list=testList)
print("Final Result 5 :: {} ".format(result))

# Test case 6
testList=[50,45,40,35,30,25,20,15,10,5]
result=reverse_list(org_list=testList)
print("Final Result 6 :: {} ".format(result))

# Test case 7
testList=[99,88,77,66,55,44,33,22,11]
result=reverse_list(org_list=testList)
print("Final Result 7 :: {} ".format(result))

# Test case 8
testList=[75,94,23,48,98,59,30,21,43,89]
result=reverse_list(org_list=testList)
print("Final Result 8 :: {} ".format(result))

# Test case 9
testList=[30,50,70,90,110,130,150,170]
result=reverse_list(org_list=testList)
print("Final Result 9 :: {} ".format(result))

# Test case 10
testList=[49,37,20,58,30,10,95,74]
result=reverse_list(org_list=testList)
print("Final Result 10 :: {} ".format(result))