# Update Dictionary
# Insert the specified item to dictionary.
# we can update the value but can't update the key

dic={2:3,6:7,4:5,7:8,5:6,3:4}
dic.update({10:20})
print(dic)

dict1= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict1["year"]=1970
print(dict1)

dict1= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict1.update({"colour":"red"})
print(dict1)


