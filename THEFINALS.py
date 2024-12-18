#Python Code that would help users know how to recycle waste

#function and classes
class Trash:
    def __init__(self, name, material, is_hazardous, is_wet):
        self.name = name
        self.material = material
        self.is_hazardous = is_hazardous
        self.is_wet = is_wet

    def disposal_recommendation(self):
        # sorting
        if self.is_hazardous:
            return "Dispose of the item at a hazardous waste facility."
        else:
            if self.material == "plastic" and not self.is_wet:
                return "Place the item in the recycling bin."
            elif self.material == "paper" and not self.is_wet:
                return "Place the item in the recycling bin."
            elif self.material == "organic":
                return "Place the item in the compost bin."
            elif self.material == "metal":
                return "Send to a metal scrap yard."
            elif self.material == "glass":
                return "Place the item in the recycling bin."
            else:
                return "Place the item in the general trash bin."

def get_yes_no(prompt):
   #boolean for hazardous and wet options
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def choose_material():
   #select material type
    print("\nSelect the material type of the item:")
    print("1. Plastic")
    print("2. Paper")
    print("3. Organic")
    print("4. Metal")
    print("5. Glass")

    while True:
        try:
            choice = int(input("Enter the number corresponding to the material type: "))
            if choice == 1:
                return "plastic"
            elif choice == 2:
                return "paper"
            elif choice == 3:
                return "organic"
            elif choice == 4:
                return "metal"
            elif choice == 5:
                return "glass"
            else:
                print("Invalid choice. Please choose a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_material_table():
#arrays
#table showing how to recycle
    disposal_table = [
        ["Plastic", "Recycling bin (if not wet)"],
        ["Paper", "Recycling bin (if not wet)"],
        ["Organic", "Compost bin"],
        ["Metal", "Metal scrap yard"],
        ["Glass", "Recycling bin"],
        ["Hazardous", "Hazardous waste facility"],
        ["Other", "General trash bin"]
    ]

    print("\n--- Material Disposal Table ---")
    print(f"{'Material':<12} | {'Disposal Recommendation'}")
    print("-" * 40)
    for row in disposal_table:
        print(f"{row[0]:<12} | {row[1]}")
    print("-" * 40)

def main():
#menu
    while True:
        print("\nWelcome to the Trash Disposal Helper!")
        print("1. Analyze an item")
        print("2. View material disposal table")
        print("3. Exit the program")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # Analyze a new item
                name = input("\nWhat is the name of the item you want to dispose of? ").strip()
                material = choose_material()
                is_hazardous = get_yes_no("Is the item hazardous")
                is_wet = get_yes_no("Is the item wet")

                item = Trash(name, material, is_hazardous, is_wet)

                # Get disposal recommendation
                recommendation = item.disposal_recommendation()

                # Display recommendation
                print(f"\nItem: {item.name}")
                print(f"Material: {item.material}")
                print(f"Hazardous: {'Yes' if is_hazardous else 'No'}")
                print(f"Wet: {'Yes' if is_wet else 'No'}")
                print(f"Recommendation: {recommendation}")

            elif choice == 2:
                # Display the material disposal table
                display_material_table()

            elif choice == 3:
                # Exit the program
                print("\nThank you for using the Trash Disposal Helper. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
