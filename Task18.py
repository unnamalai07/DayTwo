def findEndWith(num):
    try :
        print(num.endswith("0"))
    except Exception as e:
        print(f"Error : {str(e)}")


if __name__  == "__main__":
    num = input("Enter the string : ")
    findEndWith(num)