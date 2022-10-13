'''Write a function to take a list. Filter all the prime numbers, add to new list and return the new list.
    Example :
        listA=[10,20,30,40,50,60,100,11]
        result=func_exec(listA)
        print(result)
        Expected Output : [11]
    Example :
        listA=[10,20,23,30,40,50,60,100,11]
        result=func_exec(listA)
        print(result)
        Expected Output : [11,23]

    :param listA:list passed by user
    :return:Prime elements from listA
    
    Solution Steps:
    ****************
    1.From the list filter all the prime elements.
    2.Define new list for prime numbers.
    3.Iterate list and filter all prime elements.
    4.Return list prime elements.
    '''

def prime_numbers(org_list):
    # Define new list for prime values    
    prime_number =[]
    #iterate oginal list
    for i in org_list:
        #checking for number is greater than or equal to 2
        if(i>=2):
            #every prime has 2 co-factor 1 and it self number, we are taking range from 2 to 1 less the number
            # if we found any co-factors between these range this is a prime number
            for j in range(2,i):
                #checking for divisiblity if condition true loop will break
                if(i%j==0):
                    #breakdown loop
                    break
            else:
                    #if loop not breakable the number is prime and add to new list
                    prime_number.append(i)  
    #finally return
    return prime_number
                     






