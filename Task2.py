
try:
    num=int(input("Enter the number "))
    if num%2==0 :
        result="even number"

    else:
        result="odd number"
     
except Exception as e:
    result=str(e)

finally:
    print(result)