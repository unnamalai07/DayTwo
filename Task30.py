
try:
    num=int(input("Enter the number "))
    if num%2!=0 :
        if num%10==0: 
         result=f"{num} is odd number and divisible by 10."
        else:
            result=f"{num} is odd number not divisible by 20."
    else:
        result=f"{num} is not odd number"
     
except Exception as e:
    result=str(e)

finally:
    print(result)