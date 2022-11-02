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
'''

def filter_num(numx,numy,*org_list):
  new_list=[]
  for i in org_list:
       if (i%numx==0 and i%numy==0):
          new_list.append(i)
  return new_list
print (filter_num(20,10,20,40,50,60,80,90,100,70))  