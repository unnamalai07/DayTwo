try:
    num1=(input("Enter the number1 "))
    try:
        num1=int(num1)

    except:
        num1=float(num1)
       
    if num1>=50 and num1<=100 :
         if num1!=75:
            result=f"{num1} between 50 and 100 but not equal to 75."
         else:
            result=f"{num1} between 50 and 100 but  equal to 75."
   
    else:
         result=f"{num1} not between 50 and 100."
except Exception as e:
        result=str(e)

finally:
     print(result)