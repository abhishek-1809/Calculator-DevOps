import math

def display_menu():
    print("\nMenu:")
    print("1. Square root")
    print("2. Factorial")
    print("3. Natural logarithm")
    print("4. Power")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            x = float(input("Enter a number to find its square root: "))
            if x < 0:
                print("Error: Square root of a negative number is not defined.")
            else:
                print(f"Square root of {x} is {math.sqrt(x)}")
              
        elif choice == '2':
            x = int(input("Enter a non-negative integer to find its factorial: "))
            if x < 0:
                print("Error: Factorial is not defined for negative numbers.")
            else:
                print(f"Factorial of {x} is {math.factorial(x)}")
              
        elif choice == '3':
            x = float(input("Enter a number to find its natural logarithm: "))
            if x <= 0:
                print("Error: Natural logarithm is not defined for non-positive numbers.")
            else:
                print(f"Natural logarithm of {x} is {math.log(x)}")
                
        elif choice == '4':
            x = float(input("Enter the base (x): "))
            b = float(input("Enter the exponent (b): "))
            print(f"{x} raised to the power of {b} is {math.pow(x, b)}")
          
        elif choice == '5':
            print("Exiting...")
            break
          
        else:
            print("Invalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
