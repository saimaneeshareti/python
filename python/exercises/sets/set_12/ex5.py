'''
   Write a function to take 2 lists. Use zip function to iterate the list and pick values that
   are common at both indexes.

	Example :
		listA=[100,20,300,40,50,60,100]
		listB=[1100,20,1300,40,50,160,1000]
		result=func_exec(listA,listB)
		print(result)
		# 20 -> listA[1] == listB[1]
		# 40 -> listA[3] == listB[3]
		# 50 -> listA[4] == listB[4]
		Expected Output : [20,40,50]

	Example :
		listA=[1001,201,3001,401,501,601,1001]
		listB=[1100,20,1300,40,50,160,1000]
		result=func_exec(listA,listB)
		print(result)
		Expected Output : []
'''
#define a function 
def check(OrgListA,OrgListB):
    #define new list
    NewList=[]
    #iterate both lists simantanously with using zip() function
    for listA,listB in zip(OrgListA,OrgListB):
        #checking for listA element s equals to listB element
        if(listA==listB):
            #add to new list
            NewList.append(listA)
    #return new list
    return NewList

#calling function
result=check([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000])
print('Final out : {}'.format(result))

result=check([1001,201,3001,401,501,601,1001],[1100,20,1300,40,50,160,1000])
print('Final out : {}'.format(result))