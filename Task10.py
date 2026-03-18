try:
    num1=(input("Enter the number1 "))
    try:
        num1=int(num1)

    except:
        num1=float(num1)
       
    if num1>=10 and num1<=50:
         result=f"{num1} is between 10 and 50"
   
    else:
         result=f"{num1} is not between 10 and 50"
    
except Exception as e:
        result=str(e)

finally:
     print(result)