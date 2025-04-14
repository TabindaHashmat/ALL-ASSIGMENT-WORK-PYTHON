SENTENCE_START: str = "PANAVERSITY IS FUN, Learn to program and use Python to make my "

def main():
    adjective: str = input("Enter an adjective and press enter: ")
    noun: str = input("Enter a noun and press enter: ")
    verb: str = input("Enter a verb and press enter: ")
    
    print(SENTENCE_START + adjective + " " + noun + " " + verb + ".")

if __name__ == "__main__":
    main()
