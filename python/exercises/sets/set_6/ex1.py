'''
   Write a function to take a list. Filter all the prime numbers, add to new list and return the new list.
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

def check_prime(org_list):
    #define new list
    new_mapping=[]
    #iterates original list one by one
    for i in org_list:
        #checking for number is greater than Or equals to 2
        if(i>=2):        
            #every prime has 2 co-factors 1 and it self number, we are taking range from 2 to one less the number 
            # if we found any co-factors between these range this is a prime number        
            for j in range(2,i):
                #checking for Divisiblity if condition true loop will break
                if(i%j==0):
                    #breakdown loop
                    break         
            else:
                    #if loop not breakable the number is prime and adds to new list
                    new_mapping.append(i)     
    #finally return                         
    return new_mapping

#Testcase 1
result=check_prime([10,20,30,40,50,60,100,11])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 2
result=check_prime([20,10,49,20,19,30,18])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 3
result=check_prime([10,39,48,57,18,39,30,18,38])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 4
result=check_prime([18,38,49,20,40,50,29,18,40])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#Testcase 5
result=check_prime([89,20,49,10,38,18,49,30])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

#TestCase 6
result=check_prime([10,48,90,13,42,20,18,28,18])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 7
result=check_prime([20,19,38,48,75,39,20,48,95])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 8
result=check_prime([1,4,90,57,28,190,29,40,30,47])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 9
result=check_prime([19,3,2,1,89,30,57,39,28,49,2,10])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")

# TestCase 10
result=check_prime([14,30,3,2,90,40,5,19,3,6,99])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
                     






