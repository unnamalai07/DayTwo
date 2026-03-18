try:
    num1=int(input("Enter the number1 "))
    num2=int(input("Enter the number2 "))
    if num1!=num2:
        if num1<num2:
         result=f"{num1} is a samllest number"
        else:
         result=f"{num2} is a samllest number"
    else:
        result="Number is same"

except Exception as e:
        result=str(e)

finally:
     print(result)