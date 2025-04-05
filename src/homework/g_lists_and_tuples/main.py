from dictionary import get_p_distance_matrix

def main():
    dna_list = [
        ['T','T','T','C','C','A','T','T','T','A'],
        ['G','A','T','T','C','A','T','T','T','C'],
        ['T','T','T','C','C','A','T','T','T','T'],
        ['G','T','T','C','C','A','T','T','T','A']
    ]

    while True:
        print("\nMenu:")
        print("1 - Get p-distance matrix")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            matrix = get_p_distance_matrix(dna_list)
            for row in matrix:
                print(" ".join(f"{num:.5f}" for num in row))
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
