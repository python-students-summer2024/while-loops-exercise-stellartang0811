
def get_starting_number():
    while True:
        try:
            beer = int(input("How many bottles of beer on the wall? "))
            if beer >= 1:
                return beer
            else:
                print("Please input an integer 1 or greater.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def sing(num_bottles):
    num = num_bottles
    continue_singing = True
    
    while continue_singing:
        if num > 1:
            print(f"{num} bottles of beer on the wall, {num} bottles of beer.")
            if num > 2:
                print(f"Take one down, pass it around, {num -1} bottles of beer on the wall.\n")
            elif num == 2:
                print(f"Take one down, pass it around, {num -1} bottle of beer on the wall.\n")
        elif num == 1:
            print(f"{num} bottle of beer on the wall, {num} bottle of beer.")
            print(f"Take it down, pass it around, no more bottles of beer on the wall!\n")
            continue_singing = False
        num -= 1


