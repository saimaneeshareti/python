'''Write a function to take 2 lists and an integer X. Use zip function to iterate the list and pick values that
   are common at both indexes, they must be divisible by X. 
   *** Note: You must iterate the lists only if the lengths of the lists are equal. *** 
   -------------------------------------------------------------------------------------
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        numX=10
        result=func_exec(listA,listB)
        print(result)
        Expected Output : []
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[100,20,300,40,50,60,100]
        numX=20
        result=func_exec(listA,listB)
        print(result)
        Expected Output : [100,20,300,40,50,60,100]
    Example :
        listA=[100,21,300,41,50,63,100]
        listB=[100,21,300,41,50,63,100]
        numX=10
        result=func_exec(listA,listB)
        print(result)
        Expected Output : [100,300,50,100]
        
    :param orgList: Two Original list passed by the User
    :param numX: Number X passed by the User.
    :return: Pick values that are common at both indexes, they must be divisible by number X 

    Solution steps:
    ***************
    1. From the two orginal list and pick values that are common at both indexes, they must be divisible by X.
    2. Define new list for elements that are, divisible by number X.
    3. Iterate with zip function and filter the common elements .
    4. Return new list that are divisible by X in both orginal list.'''


def check_comman(orgListA,orgListB,numX):
    # define empty list    
    new_List = []
    # below condition will said both list are equal elements    
    orgListA = orgListB
    # Use zip function to iterate both the list and pick values that are common at both indexes    
    for i,j in zip(orgListA,orgListB):
    # Print the iteration elemants of the both lists        
        print(i,j)
    # check the condition the list elements are divisible by num X or not if condition is truei        
        if (i%numX!=0):
            new_List.append(i)
    return new_List


#Testcase 1
result=check_comman([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],10)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 2
result=check_comman([100,20,300,40,50,60,100],[100,20,300,40,50,60,100],20)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 3
result=check_comman([100,21,300,41,50,63,100],[100,21,300,41,50,63,100],10)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 4
result=check_comman([1,10,8,7,4,3,6,2,9,5],[32,12,8,23,27,3,62,32,21,5],5)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 5
result=check_comman([1000,800,300,500,700,100,600,400,900],[77,42,67,500,787,100,672,48,900],100)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#TestCase 6
result=check_comman([21,34,57,87,54,32,23,29,55,80],[21,13,72,87,54,43,78,90,55,88],500)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 7
result=check_comman([90,100,98,93,95,91,96,92,97,99],[76,42,67,66,34,59,42,57,63,48],4)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 8
result=check_comman([1,100,300,800,50,39,75,67,894],[1,88,76,82,35,39,75,79,86],5)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 9
result=check_comman([25,45,65,75,95,105,25,15,85],[14,35,75,88,95,78,25,71,85],3)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 10
result=check_comman([121,22,456,2337,980,432,666,77,9],[34,75,78,64,980,463,777,72,48],143)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

