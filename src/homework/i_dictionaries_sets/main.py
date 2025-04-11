from dictionary import add_inventory, remove_inventory_widget

def main():
    widgets = {}

    while True:
        print("\nInventory Menu")
        print("1- Add or Update Item")
        print("2- Delete Item")
        print("3- Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            widget_name = input("Enter widget name: ")
            quantity = int(input("Enter quantity: "))
            add_inventory(widgets, widget_name, quantity)
            print(f"Updated Inventory: {widgets}")

        elif choice == "2":
            widget_name = input("Enter widget name to delete: ")
            result = remove_inventory_widget(widgets, widget_name)
            print(result)
        
        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
