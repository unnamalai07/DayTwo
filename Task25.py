def find_smallest(num1, num2, num3):
    try:
        if num1 < num2 and num1 < num3:
            smallest = num1
        elif num2 < num1 and num2 < num3:
            smallest = num2
        else:
            smallest = num3

        print(f"The smallest number is: {smallest}")
    except Exception as e:
        print(str(e), "--- An error occurred while finding the smallest number.")

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
    except Exception as e:
        print(str(e), "--- Please enter valid numbers.")
    find_smallest(num1, num2, num3)