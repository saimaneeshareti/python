# Function: Find if a number is prime or not
#-------------------------------------------
def cal_prime(numX):
  '''
    Aim : Check if numX is prime or not
    :params:
    --------
    :param numX: An integer number
    :return:
    --------
    True if number is prime
    False if number is not prime
    :exception:
    -----------
    If numX is non-integer raise an exception
    :solution:
    ----------
  
      Example: 
      --------
      Assume numX=11
        - Any number is divisble by 1.
        - Any number is divisible by itself.
      
      Check if 11 is divisible by any number from 2 to 11
      If it's Zero, then it's not a prime.
      
      11/2 !=0
      11/3 !=0
      11/4 !=0
      11/5 !=0
      11/6 !=0
      11/7 !=0
      11/8 !=0
      11/9 !=0
      11/10 !=0
          
      Write a loop to check if numX is prime.
      
      1. From number 2 till numX, iterate and divide the 
      number by numX .
      
      2. If numX is divisible by another number, if   
      remainder is 0, return False -> Its not PRIME
      
      3. If numX is not divisible by any number, 
      if remainder > 0, return True -> Its PRIME
      
  '''
  # Write a For-LOOP for dividing numX
  for number in range(2,numX):
    print("\n")
    print("Divide {} by {} ".format(numX,number))
    divReminder=numX%number
    # If divReminder==0: NOT PRIME
    # If divReminder !=0: PRIME
    print("Division Remainder : {} ".format(divReminder))
    print("\n")
    if divReminder==0:
      # Its not a prime, return False
      return False
    else:
      # Its a prime, return True
      return True
# Execution
result=cal_prime(11)
print(result)