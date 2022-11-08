'''Write a function to take a list. Filter all the prime numbers, 
add to new list and return the new list.
Write a separate function for prime number calculcation and call it inside main function.

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
'''
def filter_prime(listA):
    new_list=[]
    for prime_num in listA:
        if(prime_num>=2):
            for i in range (2,prime_num):
                if(prime_num%i==0):
                    continue
        else:
            new_list.append(i)  
    return new_list

def cal_prime(numx):
     for i in range (2,numx):
        if(numx%i==0):
         # not a prime number
         return False            
    
                
    



print (filter_prime([10,20,30,40,50,60,100,11]))    
