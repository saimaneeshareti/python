'''
    7.From the list pick the elements that are not ODD.Add those elements to new list. Finally print the new list.
'''
# Define original list
org_list=[24,65,89,90,60,4,2,9,11,15]
# Define new list
new_lst=[]
# Iterate the list
for i in org_list:
    # Check the number is Even(not odd)
    if(i%2==0):
        # Add to new list
        new_lst.append(i)
# Finally print the new list        
print(new_lst)