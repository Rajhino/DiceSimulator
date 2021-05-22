import random

print("This is a dice simulator!")
x = "y"

while x == "y":
    face = random.randint(1, 6)
    if face == 1:
        print("----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("----------")

    elif face == 2:
        print("----------")
        print("|         |")
        print("|  0  0   |")
        print("|         |")
        print("-----------")

    elif face == 3:
        print("----------")
        print("|    0    |")
        print("| 0     0 |")
        print("|         |")
        print("----------")

    elif face == 4:
        print("----------")
        print("|    0    |")
        print("|  0   0  |")
        print("|    0    |")
        print("----------")

    elif face == 5:
        print("----------")
        print("|    0    |")
        print("| 0  0  0 |")
        print("|    0    |")
        print("----------")

    else:
        print("----------")
        print("|  0   0  |")
        print("|  0   0  |")
        print("|  0   0  |")
        print("----------")
    x = input("Tap Y to roll the dice:")

