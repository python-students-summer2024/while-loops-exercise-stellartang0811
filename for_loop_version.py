def get_starting_number():
    while True:
        try:
            beer = int(input("How many bottles of beer on the wall?"))
            if beer >= 1:
                return int(beer)
            else:
                print("Please input an integer 1 or greater.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def sing(num_bottles):
    for beer in range(num_bottles, 0, -1):
        if beer > 1:
            print(f"{beer} bottles of beer on the wall, {beer} bottles of beer.")
            if beer > 2:
                print(f"Take one down, pass it around, {beer -1} bottles of beer on the wall.\n")
            elif beer == 2:
                print(f"Take one down, pass it around, {beer -1} bottle of beer on the wall.\n")
        elif beer == 1:
            print(f"{beer} bottle of beer on the wall, {beer} bottle of beer.")
            print(f"Take it down, pass it around, no more bottles of beer on the wall!")
