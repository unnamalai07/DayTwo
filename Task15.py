def check_Number_divisible_Two_not_Five(Number):
    try :
        if (Number % 2 == 0) and (Number % 5 != 0):
            return "Given number is divisible by 2 but not divisible by 5"
        else:
            return "Given number is not divisible by 2 or is divisible by 5"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    Number = input("Enter a number: ")
    try:
        num=int(Number)
    except:
        num=float(Number)
    print(check_Number_divisible_Two_not_Five(num))
    
    