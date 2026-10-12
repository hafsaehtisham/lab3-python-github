def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Can't divide by zero"
    return a / b

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

def percentage(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return (a / b) * 100

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Even/Odd")
    print("6. Percentage")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice")
        continue

    try:
        if choice == "5":
            n = int(input("Enter number: "))
            print(even_odd(n))
        else:
            a = float(input("First number: "))
            b = float(input("Second number: "))

            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
            elif choice == "6":
                print("Result:", percentage(a, b), "%")

    except ValueError:
        print("Enter valid numbers")