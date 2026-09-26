# Developer: Hans Burton L. Damaso

def main():
    while True:
        print("\n=== Calculator Master: Gen Z version  ===")
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
                print("Bruh, ain't no way that's a number. Try again. 💀")
                continue
            
           
        else:
            print("Lowkey invalid option. Pick 1-5. ")

if __name__ == "__main__":
    main()