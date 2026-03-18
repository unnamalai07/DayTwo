
try:
    num=(input("Enter the number "))
    try:
        num=int(num)
    except:
        num=float(num)
    if num!=0:

        if num%3==0 or num%5==0:
        
            if num%3==0 and num%5==0:

                result=f"{num} is a  divisible by  3 as well as 5"
            elif  num%3==0  :
              
                result=f"{num} is a  divisible by  3 "
            else:
                result=f"{num} is a  divisible by 5"

        else:
           
            result=f"{num} is a not divisible by  3 or 5" 
    else:
  
      result="Given number is 0"

    
except Exception as e:
    result=str(e)

finally:
    print(result)