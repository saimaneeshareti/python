'''Write a function to take a list, number Y as arguments.
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
1. From the list, filter all elements from the even index and.
2. Define new list for elements that are, divisible by number Y.
3. Iterate list even Indexes array and filter all even elements and append to new array listEven.
4. Remove duplicates from array listEven.
5. Return listEven elements that are divisible by number Y. '''