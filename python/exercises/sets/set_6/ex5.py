'''Write a function to take a dict and number X as argument. Find the key,value pairs that are both divisible by number X
    Example : 
            testDict={10:20, 3:30, 4:40,90:100,20:30}
            numX=10
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {10:20,90:100,20:30}
            
        :param orgDict: Original dictionary passed by the User
        :param numX: Number X passed by the User.
        :return: New dictionary with filtered key,value pairs that are both divisible by number X.

        Solution steps:
        ***************
        1.From the orginal dict filtered key,value pairs that are both divisible by number X.
        2.Define new dict for key,value pairs,divisible by number X.
        3.Iterate dict and filter the key,value pairs.
        4.Return dict key,value filtered elements.   
            '''

def funDict(orgDict,numX):
    #  Define empty dict    
    new_Dict = {}
    # itarate the dictionary    
    for key,value in orgDict.items():
    # Below the condition will check the keys,values pairs are both divisible by number X  if condition is true it will executes if statment        
        if (key%numX==0 and value%numX==0):
    # it will add new keys,values in new dictionary            
            new_Dict[key] = value
    return new_Dict

# Execution
testDict={10:20, 3:30, 4:40,90:100,20:30}
numX=10
result=funDict(orgDict=testDict,numX=numX)
print("Final Result is :: {} ".format(result))            