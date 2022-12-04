''' Write a function to take a list. From the list find the number that occurs most number of times.
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
        
    :param list: List passed by the User
    :return: Numbers that occurs most number of times.   
    
    Solution steps:
    ***************
    1. From the orginal list and pick values that are occurs most number of times.
    2. Define new list for elements that occurs most number of times.
    3. Iterate list and filter the repeated numbers.
    4. Return new list for the number that occurs most number of times.'''
    