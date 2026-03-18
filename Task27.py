
try:
    num=(input("Enter the number "))
    try:
        num=int(num)
    except:
        num=float(num)
    if num!=0:
        if num%9==0 :
            result=f"{num} is a divisible by 9"

        else:
            result=f"{num} is a not divisible by 9"
    else:
        result="Given number is 0"
     
except Exception as e:
    result=str(e)

finally:
    print(result)