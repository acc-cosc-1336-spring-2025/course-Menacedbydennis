#from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("\nHomework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                num = int(input("Enter a number (1-9): "))
                if 1 <= num <= 9:
                    print(f"Factorial of {num} is {get_factorial(num)}") # type: ignore
                    break
                print("Invalid input. Try again.")

        elif choice == '2':
            while True:
                num = int(input("Enter a number (1-99): "))
                if 1 <= num <= 99:
                    print(f"Sum of odd numbers up to {num} is {sum_odd_numbers(num)}") # type: ignore
                    break
                print("Invalid input. Try again.")

        elif choice == '3':
            confirm = input("Do you want to exit? (yes/no): ").lower()
            if confirm == 'yes':
                break

if __name__ == "__main__":
    main()
