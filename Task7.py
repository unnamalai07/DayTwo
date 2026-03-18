try:
    age=(input("Enter the age "))
    try:
        age=int(age)
    except:
        age=float(age)
    if age>=18:
        
        result=f"{age} eligible for vote"

    else:
        result=f"{age} not eligible for vote"
  
     
except Exception as e:
    result=str(e)

finally:
    print(result)