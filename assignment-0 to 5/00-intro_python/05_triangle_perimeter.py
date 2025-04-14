def main():
    # Input with validation to ensure it's a valid number
    while True:
        try:
            side1 = float(input("Enter the length of side1: "))
            side2 = float(input("Enter the length of side2: "))
            side3 = float(input("Enter the length of side3: "))
            break  # Break the loop if all inputs are valid
        except ValueError:
            print("Invalid input! Please enter valid numbers for the sides.")
    
    # Calculate the perimeter
    perimeter = side1 + side2 + side3
    
    # Print the result
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()
