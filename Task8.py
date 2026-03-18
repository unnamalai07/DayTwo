
try:
    num=(input("Enter the number "))
    try:
        num=int(num)
    except:
        num=float(num)
    if num!=0:
        if num%10==0 :
            result=f"{num} is a multiple  by 10"

        else:
            result=f"{num} is a not multiple by 10"
    else:
        result="Given number is 0"
     
except Exception as e:
    result=str(e)

finally:
    print(result)