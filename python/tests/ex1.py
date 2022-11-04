'''
Write a function to take 2 lists and integers numX,numY .
    From the listA find all elements that are >er sum(numX+numY). Append those elements to listB.
    Remove all duplicates from listB.
    Finally sort and return listB.
   -------------------------------------------------------------------------------------
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        numX=100
        numY=10
        result=func_exec(listA,listB)
        result=(result)
        Expected Output : [20,40,50,160,300,1000,1100,1300]
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        numX=10
        numY=10
        result=func_exec(listA,listB)
        result=(result)
        Expected Output : [20,40,50,60,100,160,300,1100,1300]
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        numX=300
        numY=100
        result=func_exec(listA,listB)
        result=(result)
        Expected Output : []
        :param listA: Original listA passed by the User
        :param listB: Original listB passed by the User
        :param numx: Numberx passed by the User. Type is INT.
        :param numy: Numbery passed by the User. Type is INT.     
        :return : listB with sorted elements ONLY   
        Solution Steps :
        -----------------
        Take two lists ,NumberX and NumberY
        Iterate listA:
            Checking for whether the present  element is grater than sum of NumberX and NumberY,
            and remove duplicates from listB
            If Yes:
                Add to listB  
            else:
                continue loop                  
        Finally Sorted and return listB
'''
# define function
def check_num(listA,listB,numx,numy):
    # Iterate the list
    for element in listA:
        # check listA all elements that are >er sum(numX+numY)
        if (element>(numx+numy)):
            # Remove duplicate from listB
            if (element not in listB):
                # Add to the listB
                listB.append(element)            
    # Finally return listB
    return sorted(listB)

result=check_num([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],100,10)
print('Final Output : {}'.format(result))
result=check_num([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],10,10)
print('Final Output : {}'.format(result))
result=check_num([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],300,100)
print('Final Output  {}'.format(result))