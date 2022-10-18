'''
    4. Define a list of 10 elements. If the element is even then multiply that element by 100, 
    if the element is odd then multiply that element by 200. Finally print the new list.
'''
# Define original list
org_list=[11,100,127,99,128,331,990,23,68,10]
# Define new_list
new_lst=[]
# Iterate the list
for i in org_list:
    # Check the number even or not
    if(i%2==0):
        # If numbers is even multiply with 100 and add to the new list 
        new_lst.append(i*100)
    else:
        # If numbers is even multiply with 100 and add to the new list 
        new_lst.append(i*200)
# Print new list        
print(new_lst)
    

