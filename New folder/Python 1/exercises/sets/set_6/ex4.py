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


def funList(orgListA,orgListB,numX):
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

# Execution
testListA=[100,20,300,40,50,60,100]
testListB=[1100,20,1300,40,50,160,1000]
numX=20
result=funList(orgListA=testListA,orgListB=testListB,numX=numX)
print("Final Result is :: {} ".format(result))
