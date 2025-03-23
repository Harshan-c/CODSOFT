def add(a,b):
    c = a+b
    return c
def subtract(a,b):
    c = a-b
    return c
def Multiplication(a,b):
    c = a*b
    return c
def division(a,b):
    c = a/b
    return c
def Choice():

    operation = {
        "1" : add,
        "2" : subtract,
        "3" : Multiplication,
        "4" : division
            }

    print("Choose the operation you want to perform")
    print("1 . Add ")
    print("2 . subtract")
    print("3 . Multiplication")
    print("4 . division")

    user_choice = input("Enter your Choice: ")

    if user_choice in operation:
        try:
            num1 = int(input("enter the number 1: "))
            num2 = int(input("enter the number 2: "))
        except ValueError:
                print("Invalid input! Please enter numeric values.")
                return
        
        result = operation [user_choice](num1, num2)

        print(f"Result: {result}")
    else:
        print("Invalid choice! Please select a valid option.")

Choice()