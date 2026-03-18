try:
    num=int(input("Enter the number "))
    if num>=0 :
        result="Positive number"

    else:
        result="Negative number"
     
except Exception as e:
    result=str(e)

finally:
    print(result)