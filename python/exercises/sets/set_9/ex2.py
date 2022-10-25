'''
    2. Write a function to take a number numX, numY followed by any number of integer arguments.
    You need to find all numbers divisible by numX and numY
    Filter all the numbers from the list that are divisible numX and numY and add to new list.
    Finally return the new list.
    Note: You must use *args in your function implementation
    *******************
    Example :
        numX=20
        numY=10
        result=func_exec(numX,20,40,50,60,80,90,100,70)
        print(result)
        Expected Output : [20,40,60,80,100]
    Example :
        numX=25
        numY=5        
        result=func_exec(numX,50,60,80,90,100,70)
        print(result)
        Expected Output : [50,100]
    Example :
        numX=7
        numY=12        
        result=func_exec(numX,20,40,50,70)
        print(result)
        Expected Output : []
        :param numX: NumberX passed by the User. Type is INT.
        :param numY: NumberY passed by the User. Type is INT.
        :param integers: number of integer arguments passed by the user        
        :return: New list with filtered values ONLY. 
        
    Solution Steps :
    **************
    Define function
    Pass number X,Y and few integers using *args
    Iterates numbers *args varaible:
        Checking for divisibility integers by numberX and numberY
        if Yes:
            add to new list
        else:
            continue loop
    finally return new list         
'''
#define function
def check_div(numX,numY,*numbers):
    #define new list
    new_list=[]
    #Iterates numbers by using *args
    for i in numbers:
        #checking divisibility of number with number X and number Y
        if(i%numX==0 and i%numY==0):
            #adding to new list
            new_list.append(i)
    #Finally return new list        
    return new_list        

#calling function
#Testcase 1
result=check_div(20,10,20,40,50,60,80,90,100,70)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 2
result=check_div(25,5,50,60,80,90,100,70)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 3
result=check_div(7,12,20,40,50,70)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 4
result=check_div(8,2,3,4,5,6,7,8,9,10)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 5
result=check_div(100,100,200,300,400,500,600,700,800,900,1000)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#TestCase 6
result=check_div(50,21,22,23,24,25,26,27,28,29,30)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 7
result=check_div(10,90,91,92,93,94,95,96,97,98,99,100)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 8
result=check_div(22,11,22,33,44,55,66,77,88,99,100)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 9
result=check_div(25,35,45,55,65,75,85,95,105,115)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 10
result=check_div(121,221,321,421,521,621,721,821,921)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
