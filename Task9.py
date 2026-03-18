try:
    num1=(input("Enter the number1 "))
    num2=(input("Enter the number2 "))
    try:
        num1=int(num1)
        num2=int(num2)
        
    except:
        num1=float(num1)
        num2=float(num2)
        

    if num1>num2:
         result=f"{num1} is a greater number"
    elif num1==num2:
           result=f"{num1} and {num2} is equal" 
    else:
         result=f"{num2} is a greater number"
    

except Exception as e:
        result=str(e)

finally:
     print(result)