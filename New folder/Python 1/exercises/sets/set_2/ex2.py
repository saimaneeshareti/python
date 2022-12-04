'''Write a function to take a dict as an argument. Multiply each key by 10, each value by 5. 
Finally iterate and return the new dict.'''

def multiple(d,x,y):
  output = {}
  for key,value in d.items():
    output[key*10] = value*5
  for key, value in output.items():
    print(key,value)
  return output
print(multiple({1:2,2:3,3:4,4:5,5:6},2,3))  