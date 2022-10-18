'''
    6. Write a function to take 3 lists, numX, numY as arguments.
      If the sum of elements in the indexes is > er sum of numX + numY, then add to new list.
    Finally return the new list.
    Note: You must execute only if the lists are of same length.
    Example :
        listA=[10,20,30,40,50]
        listB=[1,2,3,4,5]
        listC=[100,150,200,250,300]
        numX=150
        numY=100
        result=func_exec(listA)
        print(result)
        Expected Output : [[40,4,250],[50,5,300]]
        Reason: 
            sum of (numX + numY) = 250
            -    sum of ([40,4,250]) is > er than sum of (numX + numY)
            -    sum of ([50,5,300]) is > er than sum of (numX + numY)
    Example :
        listA=[10,20,30,40,50]
        listB=[1,2,3,4,5]
        listC=[100,150,200,250,300]
        numX=50
        numY=100
        result=func_exec(listA)
        print(result)
        Expected Output : [[20,2,150], [30,3,200], [40,4,250],[50,5,300]]
        Reason:
            sum of (numX + numY) = 150 
            -    sum of ([20,2,150]) is > er than sum of (numX + numY)
            -    sum of ([30,3,200]) is > er than sum of (numX + numY)                        
            -    sum of ([40,4,250]) is > er than sum of (numX + numY)
            -    sum of ([50,5,300]) is > er than sum of (numX + numY)
    Example :
        listA=[10,20,30,40,50]
        listB=[1,2,3,4,5]
        listC=[100,150,200,250,300]
        numX=500
        numY=100
        result=func_exec(listA)
        print(result)
        Expected Output : []
        Reason: 
           sum of (numX + numY) = 600
           Sum of values in the indexes are < 600
    Solution Steps:
    **************
    Take three list and iterate simantanously
        checking sum of numbers in same indexes of three list is greater sum of number X and number Y  
        if Yes:
            add numbers as list to new list
        else:
            continue loop
    finally return new list             
'''
#define function
def sum_list(Org_listA,Org_listB,Org_listC,numX,numY):
    #define new list
    new_list=[]
    #iterate three lists simantanously
    for listA,listB,listC in zip(Org_listA,Org_listB,Org_listC):
        #checking condition for sum of same indexes numbers in three lists is greater than sum of number x and number y
        if((listA+listB+listC)>(numX+numY)):
            #adding numbers as list into new list
            new_list.append([listA,listB,listC])
    #fiinally return new list        
    return new_list    

#Testcase 1
result=sum_list([10,20,30,40,50],[1,2,3,4,5],[100,150,200,250,300],150,100)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 2
result=sum_list([10,20,30,40,50],[1,2,3,4,5],[100,150,200,250,300],50,100)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 3
result=sum_list([10,20,30,40,50],[1,2,3,4,5],[100,150,200,250,300],500,100)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 4
result=sum_list([1,8,4,3,55],[32,12,32,21,5],[32,23,29,55,80],100,200)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 5
result=sum_list([1000,800,300,500,200],[39,500,588,23,569],[43,78,90,55,88],200,300)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#TestCase 6
result=sum_list([32,23,29,55,80],[54,43,78,90,55],[15,45,34,22,65,34],400,200)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 7
result=sum_list([20,49,2,134,45,23],[76,42,67,66,34],[100,300,800,50,39],55,45)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 8
result=sum_list([1,100,300,800,50],[1,88,76,82,35],[39,75,67,89,45],800,100)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 9
result=sum_list([25,45,65,75,95],[14,35,75,88,95],[78,25,71,85,10],200,100)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 10
result=sum_list([121,22,456,980],[666,77,90,10],[34,75,78,72,48],150,160)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
