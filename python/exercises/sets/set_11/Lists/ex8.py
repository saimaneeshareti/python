# Deletion:
# Delete the specify item from the list

listA=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
del listA[4]
print(listA)

listB = [5,10,15,20,25,30,35,40,45,50]
del listB[-1]
print(listB)

listC=[2,3,4,5,6,7,8,9,10,11,12]
del listC[:2] 
print(listC)

listD=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
del listD[3:]
print(listD)

listE = [5,10,15,20,25,30,35,40,45,50]
del listE[2:6]
print(listE)

listF=[2,3,4,5,6,7,8,9,10,11,12]
del listF[:] 
print(listF)