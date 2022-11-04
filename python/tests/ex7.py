'''
    Write a function to take a dict as argument. Sort the dict by values and return the dict.
	Example : 
			testDict={1:4,10:20,3:40,4:7,60:11,12:9}
			result=func_exec(testDict)
			print(result)
			Expected Output : {1:4,4:7,12:9,60:11,10:20,3:40}
            :param org_dic: Original dictionary passed by the User
            :return: New dic with filtered values ONLY
Solution Steps:
**************
Define the the function 
  We can take one empty dictionary
  Sort the dictionary value and store in variable
  Iterate the original dictionary
  Sorted values are add to the empty dictionary 
  Return the empty dictionary 
Print empty dictionary  
'''
#define a function 
def check(dic):
    #define new dict
    NewDic={}
    #stores values from original dict in sorted list
    values=sorted(dic.values())
    #iterates values from values sorted list
    for val in values:
        #iterates keys and values from original dict simantanously
        for _key,_value in dic.items():
            #checking if the sorted value is equals to original dict value
            if(val==_value):
                #add to new dic
                NewDic[_key]=_value
    #finally return new dict
    return NewDic

#calling function
result=check({1:4,10:20,3:40,4:7,60:11,12:9})
print('Finall output : {}'.format(result))