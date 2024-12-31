name = input("What is your name? ")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Snake")
    case _:
        print("Who dis?")