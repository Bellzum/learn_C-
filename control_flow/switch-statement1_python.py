def main():
    print("What is your favorite winter sport?: \n")
    print("1.Skiing\n2:Sledding\n3:Sitting by the fire\n4.Drinking hot chocolate\n")
    menu_item = input("Enter a valid number: ")
    #switch in cpp = match in python
    match menu_item:
        case 1: print("Skiing?! Sounds dangerous!")
        case 2: print("Sledding?! Sounds like work!")
        case 3: print("Sitting by the fire?! Sounds warm!")
        case 4: print("Hot chocolate?! Yum!")
        case _: print("Enter a valid menu item")

    begin = input("\nWhere do you want to begin?\n"
                    "B. At the beginning?\n"
                    "M. At the middle?\n"
                    "E. At the end\n\n"
                    "Enter B, M, or E: ").strip().upper()

    match begin:
        case "B": print("Once upon a time there was a wolf.")
        case "M": print("The wolf hurt his leg.")
        case "E": print("The wolf lived happily ever after")
        case _:   print("Please enter B, M, or E")
if __name__ == "__main__":
    main()