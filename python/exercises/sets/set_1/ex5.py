'''
    5. Define a list of 10 elements. From the list pick the elements that are not divisible by 5. 
    Add those elements to new list. Finally print the new list.
'''
# Define original list
org_list=[11,100,127,99,125,331,990,23,68,10]
# Define new_list
new_lst=[]
# Iterate the list
for i in org_list:
    # Check condition for number is not divisible by 5
    if(i%5!=0):
        # Add to the new list
        new_lst.append(i)
# Print the new list        
print(new_lst)