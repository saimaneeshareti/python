'''
    Write a function to calculate the employee hike based on appraisal rating.
   
    Note: 
       1. You must use **kwargs
       2. If the rating score is >100 for any employee you must raise exception since max allowed score is 100 ONLY
       3. If the input score is non-integer, you must raise exception since scores can be in integers ONLY
   ----------------------------------------------------------------------------------------------------------------
    Here's the table to calculcate the hike
       Total       Hike%
       ------      ------
        100         30
        90-100      24
        80-90       17
        70-80       12
        60-70       8
        50-60       4
        <50         1
    Example :
        result=func_exec(rating=100,curr_salary=100000)
        print(result)
        Expected Output : {"hike":"30","new_dic_salary":"130000"}
    Example :
        result=func_exec(rating=49,curr_salary=100000)
        print(result)
        Expected Output : {"hike":"1","new_dic_salary":"101000"}
    Example :
        result=func_exec(rating=200,curr_salary=50000)
        print(result)
        Expected Output : Raise Exception since rating score is 200, max allowed rating score is 100 ONLY
    Example :
        result=func_exec(rating="100",curr_salary=50000)
        print(result)
        Expected Output : Raise Exception since rating score is a string "100", rating scores can be integers ONLY
**kwargs :
    - The **kwargs arguments are passed as a dictionary and these arguments like key and value
    - We can pass a variable number of arguments to a function using special **kwargs                
    :param **appr: a **kwarg appr given by the User.as rating and cur_salary
    :return :return new salary as per rating with addition of hike%
    Solution Steps:
    **************
    Take a **kwarg with rating and current salary.
    Check max allowed score is 100 Only
    Check scores can be in integers Only
    Check for hike categories as per rating.
    Finally return new salary with addition of hike.
'''
#define a function with arguments **kwargs
def check(**appr):
    
    #assigined rate from appr
    rate=appr['rating']
    #assigned salary from appr
    salary=appr['cur_salary']
    
    #checking whether the rate is NON-integer type
    if(type(rate)==str or type(salary)==str):
      return ('Scores can be in integers only')
    #checking whether the rate is greater than 100
    elif(rate>100):
      return 'Max allowed score is 100 ONLY'
    #checking wheter the rate is 100
    elif(rate==100):
    #reurn new_dic salary with extra 30%
      return {'hike':rate,'new_salary':salary+(30*salary/100)}
    #checking whether the rate is less than 100 and greater than or equal to 90
    elif(rate<100 and rate>=90):
      #return new_dic salary with extra 24%
      return {'hike':rate,'new_salary':salary+(24*salary/100)}
    #checking whether the rate is less than 90 and greater than or equals to 80
    elif(rate<90 and rate>=80):
      #return new_dic salary with extra 17%
      return {'hike':rate,'new_salary':salary+(17*salary/100)}
    #checking whether the rate less than 80 and greater than or equals to 70
    elif(rate<80 and rate>=70):
      #return new_dic salary with extra 12%
      return{'hike':rate,'new_salary':salary+(12*salary/100)}
    #checking whether the rate less than 70 and greater than or equals to 60
    elif(rate<70 and rate>=60):
      #return new_dic salary with extra 8%
      return {'hike':rate,'new_salary':salary+(8*salary/100)}
    #checking whether the rate is less than 60 and greaater than or equals to 50
    elif(rate<60 and rate>=50):
      #return new_dic salary with extra 4%
      return {'hike':rate,'new_salary':salary+(4*salary/100)}
    #checking whether the rate is less than 50
    elif(rate<50):
        #return new_dic salary with extra 1%
      return {'hike':rate,'new_salary':salary+(1*salary/100)}

#Calling Function       
result=check(rating=100,cur_salary=100000)
print(result)

result=check(rating=49,cur_salary=100000)
print(result)

result=check(rating=200,cur_salary=50000)
print(result)

result=check(rating='100',cur_salary=100000)
print(result)