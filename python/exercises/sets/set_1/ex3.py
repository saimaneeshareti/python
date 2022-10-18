'''
    3.Define a dictionary with 10 keys. If the dict key is > 10, then add it to new dict.Finally iterate and print the new dict.
'''
# Define original dictionary
org_dic={11:1,9:2,8:3,0:4,76:5,5:6,4:7,3:8,922:9,911:10}
# Define new dictionary
new_dct={}
# Iterate the dictionary
for _key,_value in org_dic.items():
    # Check, if key is greater than 10 
    if(_key>10):
        # update the key
        new_dct[_key]=_value
# print the new dictionary        
print(new_dct)
