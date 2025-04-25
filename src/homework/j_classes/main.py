from class_a import Die

def main():
    die = Die()
    while True:
        input("Press Enter to roll the die...")
        die.roll()
        print(die)

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
