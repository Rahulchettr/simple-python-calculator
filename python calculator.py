import math

def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Multiply(x, y):
    return x * y

def Divide(x, y): 
    if y != 0:
        return x / y
    else:
        return " cannot divide any negative number ."

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def Square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Cannot take a square root of negative number."

# MAIN LOOP
while True:
    print("\nSelect operator")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Square Root (√x)")
    print("8. Exit")
    

    choice = input("Enter your choice (1 - 8): ")

    if choice == "8":
        print("Exiting calculator. Goodbye!")
        break

    elif choice == "7":
        num = float(input("Enter a number: "))
        print("Result:", Square_root(num))

    elif choice in ["1", "2", "3", "4", "5", "6"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", Add(num1, num2))
        elif choice == "2":
            print("Result:", Subtract(num1, num2))
        elif choice == "3":
            print("Result:", Multiply(num1, num2))
        elif choice == "4":
            print("Result:", Divide(num1, num2))
        elif choice == "5":
            print("Result:", modulus(num1, num2))
        elif choice == "6":
            print("Result:", power(num1, num2))

    else:
        print("Invalid input. Please enter a number between 1 and 8.")
        break
