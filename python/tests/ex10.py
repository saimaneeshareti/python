'''
   Write a function to take a dict as argument. Sort the dict by values and return the dict.
    Example : 
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,4:7,12:9,60:11,10:20,3:40}
'''
def sort_by_value(dict):
    new_dict={}
    for _value in sorted(dict.value):
        new_dict.update({key:dic[_value]})
    return new_    