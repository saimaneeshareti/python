'''
   6.Define a list of 10 elements. From the list pick the elements that are not divisible by 5 and 3. 
   Add those elements to new list. Finally print the new list.
'''
# Define Original list
org_list=[11,100,127,99,125,331,990,23,68,10]
# Define new list
new_lst=[]
# Iterate the list
for i in org_list:
    # Condition for number is not divisible by 5 and 3
    if(i%5!=0 and i%3!=0):
        # Add to new list
        new_lst.append(i)
# Print new list        
print(new_lst) 