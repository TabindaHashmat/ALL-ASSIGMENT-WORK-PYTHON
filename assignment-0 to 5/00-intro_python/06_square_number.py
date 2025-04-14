def main():
    number = float(input("\033[1;3m Type number to see square: \033[0m"))
    
    square = number * number  # Calculate square first
    print(f"The square of {number} is {square}")  # Then print it

if __name__ == "__main__":
    main()
