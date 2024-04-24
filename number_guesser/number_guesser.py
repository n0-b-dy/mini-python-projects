import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please type a number large than 0 next time.')
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess again: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    
    
    if user_guess == random_number:
        print("You got it! HORRAY!!!! WOOHOOOO!!!!!!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
    
    
    
    # else:
    #     print("You got it WRONG!!!!! MUWAHAHAHAHHAHAHAHAHA")

print("Dang man it took you", guesses, "guesses")







