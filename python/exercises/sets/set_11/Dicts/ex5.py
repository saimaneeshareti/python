# Sorting by values:
# Arranging Ascending order of values

dic={2:4,22:40,1:20,19:30}
# Define new dict
new_dic={}
# Sorted keys are assign to _keys variable
_val=sorted(dic.values())

#iterates values one by one
for _keys in _val:
    #iterates keys from original dict one by one
    for _val in dic:
        #checking for values and keys if condition true it adds to new dict.
        if(_keys==dic[_val]):
            #add key-value pair to new dictionary
            new_dic[_val]=_keys
# Print new_dict            
print(new_dic)            