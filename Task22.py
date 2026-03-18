
try:
    num=(input("Enter the number "))
    try:
        num=int(num)
    except:
        num=float(num)
    if num!=0:

        if num%4==0 and num%6==0:
        
            result=f"{num} is a divisible by  4 and 6"

        else:
            if num%4==0 and num%6!=0:

                result=f"{num} is a  divisible by  4 but not divisible by 6"

            elif num%4!=0 and num%6!=0:
                result=f"{num} is a  not divisible by  4 and not divisible by 6"

            else:
                result=f"{num} is a not divisible by  4 but  divisible by 6" 
    else:
  
      result="Given number is 0"

    
except Exception as e:
    result=str(e)

finally:
    print(result)