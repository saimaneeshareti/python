'''
    1.Write a function to take a list, numX, numY as arguments.
      Filter all the numbers from the list that are >numX and <numY and add to new list.
      Finally return the new list.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [50]
        Reason: 50 is >er than numX 45 and <er than numY 55
    Example :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [46,52,54]
        Reason: 46 is >er than numX 45 and <er than numY 55
        Reason: 52 is >er than numX 45 and <er than numY 55
        Reason: 54 is >er than numX 45 and <er than numY 55
    Example :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=450
        numY=550
        result=func_exec(listA)
        print(result)
        Expected Output : []

    :param listA: List passed by the User
    :return: The number from the list that is greater than numX and less than numY.

    Solution Steps:
    **************
    listA=[10,20,30,40,50,60,100,11,12,13]
    Iterate the list -> listA:
        Find the current number, store in a variable currNumber
        Find the sum of remaining numbers and store in a variable sumList
        Check if currNumber is >erX and <erY :
            If yes:
                return currNumber
            else:
                continue the LOOP   

'''

def check_num(org_list,numX,numY):
    #define new list
    new_list=[]
    #iterate elements from orig_list one by one
    for i in org_list:
    #check the element for greater than numx and less than numy
        if(i>numX and i<numY):
    #adding element to new list
            new_list.append(i)
    #finally return new list
    return new_list

# Test case 1
x=check_num([22,12,32,42,40,45,35,2,5],25,35)
print('final output 1 : {}'.format(x))  

# Test case 2
x=check_num([10,20,30,46,52,60,54,11,12,13],25,35)
print('final output 2 : {}'.format(x))  

# Test case 3
x=check_num([10,20,30,40,50,60,100,11,12,13],25,35)
print('final output 3 : {}'.format(x))  

# Test case 4
x=check_num([39,10,28,30,48,19,20,37,16,20],15,35)
print('final output 4 : {}'.format(x))  

# Test case 5
x=check_num([10,28,37,47,91,93,48,19,18,10],25,5)
print('final output 5 : {}'.format(x))  

# Test case 6
x=check_num([19,29,37,56,72,10,20,38],15,5)
print('final output 6 : {}'.format(x))

# Test case 7
x=check_num([8,19,30,48,29,40,58,10,20,48],25,15)
print('final output 7 : {}'.format(x))

# Test case 8
x=check_num([20,38,15,39,19,40,20,58,19],10,5)
print('final output 8 : {}'.format(x))

# Test case 9
x=check_num([91,30,4,2,80,10,49,30,10,40,58],14,10)
print('final output 9 : {}'.format(x))

# Test case 10
x=check_num([19,30,49,20,50,78,20,44,82,79],9,5)
print('final output 10 : {}'.format(x))