# Iteration
#Repeated execution of a set of statements with the help of loops is called iteration.
 
# list iteration
listA=[2,4,6,8,10,12,14,16,18,20]
for i in listA:
    print('list iteration :',i)
    #print('list iteration :'i,end=' ')

# Append Iteration
listA=[1, 2,3,4,5]
listB=[11,12,13,14,15]
for i in listB:
    listA.append(i)
print('list Append :',listA)


# Index iteration
listA=[1000,900,800,700,600]
for i in range(len(listA)):
    print('Index number: ',i)  
    #print('list iteration :'i,end=' ')

# Sorting iteration
listA=[10,20,5,15,25,30,25]
for i in sorted(listA):
    print('sorted list: ',i)
    #print('list iteration :'i,end=' ')