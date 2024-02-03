import random as r

def generator():

    lower_limit_chosen = False
    upper_limit_chosen = False

    while not lower_limit_chosen:
        try:
            lower_limit = int(input("\nGib eine Untergrenze ein: "))
            lower_limit_chosen = True
        except ValueError:
            print(f"Bitte gib eine Ganzzahl ein.")

    while not upper_limit_chosen:
        try:
            upper_limit = int(input("\nGib eine Obergrenze ein: "))
            if upper_limit <= lower_limit:
                print(f"Bitte gib eine Ganzzahl ein die über der unteren Grenze liegt.")
            else:
                upper_limit_chosen = True
        except ValueError:
            print(f"Bitte gib eine Ganzzahl ein.")

    random_number = r.randint(lower_limit,upper_limit)

    print(f"\n\nDeine Zufallszahl lautet: {random_number}\n")

if __name__ == "__main__":
    generator()