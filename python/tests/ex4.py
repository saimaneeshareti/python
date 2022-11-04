'''
Write a function to take a number numX, numY followed by any number of integer arguments.
    You need to find all numbers divisible by numX and numY
    Filter all the numbers from the list that are divisible numX and numY and add to new list.
    Finally return the new list.
    Note: You must use *args in your function implementation
    *********************************************************
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
* Args :
    - The *args can be really useful, it allows you to pass a varying number of positional arguments
    - *args allows to more arguments than the number of arguments that you previously defined Variable
    -  Python has *args which allow to pass number arguments to function.
        :param numx: Numberx passed by the User. Type is INT.
        :param numy: Numbery passed by the User. Type is INT.   
        :param *numbers: Numbers are passed by the User. Type is INT.  
        :return : return new list with fltered elements ONLY  
    Solution Steps:
    **************
    Iterate the the numbers by using *args(*numbers) 
        Check the numbers are divisible by numx and numy
        if Yes:
            add to new list
        else:
            continue loop
    Finally return the new list       
'''
# Define function
def check_num(numx,numy,*numbers):
    # Define new list
    new_list=[]
    # Iterate the numbers 
    for element in numbers:
        # Check numbers are divisible by numx and numy
        if (element%numx==0 and element%numy==0):
            # Add to new list
            new_list.append(element)
    # Finally return new listS        
    return new_list

result=check_num(20,10,20,40,50,60,80,90,100,70)  
print('Final Output : {}'.format(result)) 
result=check_num(25,5,50,60,80,90,100,70)
print('Final Output : {}'.format(result))
result=check_num(7,12,50,60,80,90,100,70)
print('Final Output : {}'.format(result))