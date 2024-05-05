name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are walking down the street at night on a cold autumn night and there is a fork in the road which way do you go (left/right)? ").lower()

if answer == "left":
    answer = input(
        "You come to a cornfield do you walk into it or around it? Type 'walk' to walk around or 'through' go through: ")

    if answer == "through":
        print("You were abducted by the creeper and dragged deeper into the cornfield")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
        
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)