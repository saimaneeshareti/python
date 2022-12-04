'''Write a function to take a dict, number X and number Y as arguments. Multiply each key by number X, each value by number Y. 
Finally iterate and return the new dict.
'''

def function_dict(dict_d,x,y):
  output = {}
  for key, value in dict_d.items():
    output[key*x] = value*y
  for key, value in output.items():
    print(key,value)
  return output
print(function_dict({1:3,5:7,9:10,12:15,20:25},2,3))
