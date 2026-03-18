
try:
    num=(input("Enter the age "))
    try:
        num=int(num)
    except:
        num=float(num)
   
    if num<13:
       result="unna is a child"
    elif  num>=13 and num<=18:
        result="unna is a  teenage"
    else:
        result="unna is a  adult"
      
        
except Exception as e:
    result=str(e)

finally:
    print(result)