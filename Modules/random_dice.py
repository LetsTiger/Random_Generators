import random as r

dice = {
    1: "+-------+\n|       |\n|   •   |\n|       |\n+-------+",
    2: "+-------+\n| •     |\n|       |\n|     • |\n+-------+",
    3: "+-------+\n| •     |\n|   •   |\n|     • |\n+-------+",
    4: "+-------+\n| •   • |\n|       |\n| •   • |\n+-------+",
    5: "+-------+\n| •   • |\n|   •   |\n| •   • |\n+-------+",
    6: "+-------+\n| •   • |\n| •   • |\n| •   • |\n+-------+"
}

def generator():
    chosen_eyes = r.randint(1,6)

    print(f"\n{dice[chosen_eyes]}")

if __name__ == "__main__":
    generator()