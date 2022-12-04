'''Define a dictionary with 10 keys. If the dict key is > 10, then add it to new dict. 
Finally iterate and print the new dict.'''

d1={45:9,89:94,60:78,70:54,54:9,89:4,96:3,73:2,45:8,87:5}
d2={}
for key,value in d1.items():
  if(key>10):
    d2[key]=value
for keys in d2.keys():
  print(key)
print(d2)

