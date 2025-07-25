print("Select the number of Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter Operation No. : "))
number1= int(input("Enter First Value: "))
number2= int(input("Enter Second Value: "))

match choice:
    case 1:
        print("Result: ", number1 + number2)
    case 2:
        print("Result: ", number1 - number2)
    case 3:
        print("Result: ", number1 * number2)
    case 4:
        print("Result: ", number1 / number2)
    case _:
        print("Choose a valid option!")