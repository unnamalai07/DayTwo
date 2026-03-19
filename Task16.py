def find_largest(num1, num2, num3):
    try:
        if num1 >= num2 and num1 >= num3:
            largest = num1
        elif num2 >= num1 and num2 >= num3:
            largest = num2
        else:
            
            largest = num3
        print(f"The largest number is: {largest}")
    except Exception as e:
        print(str(e), "--- An error occurred while finding the largest number.")


if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        find_largest(num1, num2, num3)
    except Exception as e:
        print(str(e), "--- Please enter valid numbers.")