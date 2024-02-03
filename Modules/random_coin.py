import random as r

def generator():
    result = r.choice(["Kopf","Zahl"])

    print(f"\nErgebnis: {result}")

if __name__ == "__main__":
    generator()