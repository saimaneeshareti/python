# Sorting by keys:
# Arranging Ascending order of keys

dic={8:9,30:49,10:20,22:38}
# Define new dict
new_dic={}
# Sorted keys are assign to _keys variable
_keys=sorted(dic.keys())

# Iterate the keys
for i in _keys:
    # Update new dictionary
    new_dic[i]=dic[i]
# print new dict    
print(new_dic)
    