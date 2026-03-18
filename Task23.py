

try:
    num1=(input("Enter the number1 "))
   
    try:
        num1=int(num1)

    except:
        num1=float(num1)

       
    if num1>100 or num1<50:
         
        if num1>100:
          result=f"{num1} is greater than 100"

        else:
             result=f"{num1} is less than 50"
                  
    else:
         result=f"{num1} is not greater than 100 or less than 50"

    
except Exception as e:
        result=str(e)

finally:
     print(result)