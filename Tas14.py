

try:
    num1=(input("Enter the number1 "))
    try:
        num1=int(num1)

    except:
        num1=float(num1)
       
    if num1>0:
         result=f"{num1} is positive"

    elif num1<0:
        result=f"{num1} is negative" 
   
    else:
         result=f"{num1} is 0"
    
except Exception as e:
        result=str(e)

finally:
     print(result)