'''
    2. Write a function to take a list. 
       Select the number from the list that is greater than sum of all other numbers.
        Example :
            listA=[1,2,13,4,5]
            result=func_exec(listA)
            print(result)
            Expected Output : 13
            Reason: 13 is greater than sum of [1,2,4,5] -> 12
    
        Example :
            listA=[100,20,300,40,1000,50,60,100]
            result=func_exec(listA)
            print(result)
            Expected Output : 1000
            Reason: 1000 is greater than sum of [100,20,300,40,50,60,100] -> 670
            :param org_list: Original list passed by the User        
            :return: New list with filtered values ONLY
    :param listA: List passed by the User
    :return: The number from the list that is greater than sum of all other numbers.
    
    Solution Steps:
    ----------------
    listA=[1,2,13,4,5]
    Iterate the list -> listA:
        Find the current number, store in a variable currNumber
        Find the sum of remaining numbers and store in a variable sumList
        Check if currNumber is >er sumList:
            If yes:
                return currNumber
            else:
                continue the LOOP        
'''