
try:
    num=int(input("Enter the number "))
    if num%2==0 :
        if num>20: 
         result=f"{num} is even number  greater than 20."
        else:
            result=f"{num} is even number not greater than 20."
    else:
        result=f"{num} is not even number"
     
except Exception as e:
    result=str(e)

finally:
    print(result)