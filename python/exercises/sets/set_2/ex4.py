'''Write a function to take a dict, number X as arguments. If the dict key is > number X, then add it to new dict. 
Finally iterate and return the new dict.'''

def function_dict(dict_d,x):
  output = {}
  l2 = []
  for key, value in dict_d.items():
    if(key>x):
      output[key] = value
  for key, value in output.items():
    print(key,value)
  return output
print(function_dict({1:3,5:7,9:10,12:15,20:25},2))