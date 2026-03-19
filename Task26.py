def isuppercase_IsLowercase(char):
    try:
        if char.isupper():
            print(f"{char} is an uppercase character.")
        elif char.islower():
            print(f"{char} is a lowercase character.")
        else:
            print(f"{char} is not an alphabetic character.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    character = input("Enter a character: ")
    isuppercase_IsLowercase(character)