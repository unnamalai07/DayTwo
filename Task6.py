
# Need to check whether the given number is divisible by 3 and 7 or not.
try:
    num=(input("Enter the number "))
    try:
        num=int(num)
    except:
        num=float(num)
    if num!=0:

        if num%3==0 and num%7==0:
        
            result=f"{num} is a divisible by  3 and 7"

        else:
            if num%3==0 and num%7!=0:

                result=f"{num} is a  divisible by  3 but not divisible by 7"

            elif num%3!=0 and num%7!=0:
                result=f"{num} is a  not divisible by  3 and not divisible by 7"

            else:
                result=f"{num} is a not divisible by  3 but  divisible by 7" 
    else:
  
      result="Given number is 0"

    
except Exception as e:
    result=str(e)

finally:
    print(result)