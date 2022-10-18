'''
    2. Define a dictionary with 10 keys. Multiply each key by 10, each value by 5.Finally iterate and Print the new dict.
'''
# Define original dictionary
org_dic={10:1,9:2,8:3,7:4,6:5,5:6,4:7,3:8,2:9,1:10}
#define a new dictionary
new_dic={}
#Iterate the dictionary
for _key,_value in org_dic.items():
        #Multiply each key by 10, each value by 5
        new_dic[_key*10]=_value*5
# Finally print new dictionary        
print(new_dic)
