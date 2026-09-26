# Developer: Hans Burton L. Damaso BIT41

def add(a, b):
    """Calculates the total glow up of two numbers."""
    return a + b

def subtract(a, b):
    """Finds the leftover vibe after cancelling."""
    return a - b

def multiply(a, b):
    """Stacks up the product of two numbers."""
    return a * b

def divide(a, b):
    """Splits the tea evenly between two numbers."""
    return a / b

def main():
    while True:
        print("\n===  Calculator Master: Gen Z version  ===")
        print("1. Glow up (Addition)")
        print("2. Cancel (Subtraction)")
        print("3. Stack 'em (Multiplication)")
        print("4. Split the tea (Division)")
        print("5. Dip (Exit)")

        choice = input("What's the move? Select (1-5): ")

        if choice == "5":
            print("Aight, bet. Catch you later! ")
            break
        elif choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Drop the first number: "))
                num2 = float(input("Drop the second number: "))
            except ValueError:
                print("Bruh, ain't no way that's a number. Try again. ")
                continue
            
            if choice == "1":
                print(f"Periodt! The total glow up is: {add(num1, num2)} ")
            elif choice == "2":
                print(f"Oof, cancelled. We are left with: {subtract(num1, num2)} ")
            elif choice == "3":
                print(f"Big W! Stacked up, it's giving: {multiply(num1, num2)} ")
            elif choice == "4":
                try:
                    print(f"Spilling the tea... everyone gets: {divide(num1, num2)} ")
                except ZeroDivisionError:
                    print("Bro, you can't divide by zero. That's a mega red flag. ")
        else:
            print("Lowkey invalid option. Pick 1-5. ")

if __name__ == "__main__":
    main()