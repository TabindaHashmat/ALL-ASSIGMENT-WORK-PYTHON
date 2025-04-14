# Constants
C = 299_792_458  # Speed of light in meters per second

def main():
    try:
        # Prompt user for mass input
        mass_in_kg = float(input("Enter mass in kilograms: "))
        if mass_in_kg < 0:
            print("Mass cannot be negative.")
            return

        # Calculate energy using E = mc^2
        energy_in_joules = mass_in_kg * (C ** 2)

        # Display results
        print("\ne = m * c^2")
        print(f"m = {mass_in_kg} kg")
        print(f"c = {C} m/s")
        print(f"Energy = {energy_in_joules:,.3e} joules")

    except ValueError:
        print("Invalid input. Please enter a numeric value for mass.")

if __name__ == '__main__':
    main()
