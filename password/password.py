import random
import string

def generate_password(length, complexity):
    if complexity == 'simple':
        characters = string.ascii_lowercase 
    elif complexity == 'medium':
        characters = string.ascii_letters 
    elif complexity == 'complex':
        characters = string.ascii_letters + string.digits + string.punctuation 
    else:
        return "Invalid complexity level."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of your password: "))
    complexity = input("Enter complexity (simple, medium, complex): ").lower()

    password = generate_password(length, complexity)

    print(f"Generated password is: {password}")

if __name__ == "__main__":
    main()
