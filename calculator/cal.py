def add(a, b):
    c = a + b
    return c

def subtract(a, b):
    c = a - b
    return c

def Multiplication(a, b):
    c = a * b
    return c

def division(a, b):
    c = a / b
    return c

def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def Choice():
    operation = {
        "1": add,
        "2": subtract,
        "3": Multiplication,
        "4": division
    }

    print("Choose the operation you want to perform")
    print("1 . Add")
    print("2 . Subtract")
    print("3 . Multiplication")
    print("4 . Division")

    while True:
        user_choice = input("Enter your Choice (1-4): ")
        
        if user_choice in operation:
            num1 = get_valid_number("Enter number 1: ")
            num2 = get_valid_number("Enter number 2: ")
            
            if user_choice == "4" and num2 == 0:
                print("Error: Cannot divide by zero!")
                continue
                
            result = operation[user_choice](num1, num2)
            print(f"Result: {result}")
            break
        else:
            print("Invalid choice! Please select a valid option.")

while True:
    Choice()
    again = input("Do you want to perform another calculation? (y/n): ").lower()
    if again != 'y':
        print("Thanks for using")
        break