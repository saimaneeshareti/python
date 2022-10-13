'''Define a dictionary with 10 keys. Multiply each key by 10, each value by 5. 
Finally iterate and Print the new dict.'''

d1={45:9,89:94,60:78,70:54,54:9,89:4,96:3,73:2,45:8,87:5}
d2={}
for key,value in d1.items():
  if(key>10):
    d2[key*10]=value*5
for keys in d2.keys():
  print(key)
print(d2) 
