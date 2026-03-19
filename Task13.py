def is_leap_year(year):
    try :
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
            return False
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    try :
        year = int(input("Enter a year: "))
    except Exception as e:
        print(str(e), "--- Please enter a valid integer for the year.")
    is_leap_year(year)
        