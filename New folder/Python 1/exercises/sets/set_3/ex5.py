'''Write a function to take a dict, number X,Y as arguments. If the prod of (dict key * dict val) is > sum of number (X+Y), 
then add it to new dict.Finally iterate and return the new dict.'''

def product(org_dic,numx,numy):
#Define an empty new dictionary
  new_mapper={} 
# Iterate the original dictionary and filter the values
  for _key,_val in org_dic.items(): 
# if the condition is product of keyand value is greterthan sum of numx,numy
    if (_key*_val>numx+numy): 
# If the condition is satisfied, add the key & value to the new dictionary
      new_mapper[_key]=_val
#Finally return the new dic
  return new_mapper 

# Execution
testDict={1:4,10:2,3:4,4:7,6:11,12:9}
numx=20
numy=30
result=product(org_dic=testDict,numx=numx,numy=numy)
print("Final Result is :: {} ".format(result))