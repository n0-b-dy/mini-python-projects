print ("Hey man, wanna expand your knowledge, so you can insult people on the interwebz?")

playing = input("Well, do ya? ('y or n)")

if playing.lower() != "y":
    quit()

print("Alright, let's ride")
score = 0

# Question 1
answer = input("A lower-functioning subspecies cave-dwelling humanoid that usually inhabits subterranean dwellings, and enjoys frequenting Wal-Mart. They tend to chiefly subsist on some form of government/taxpayer assistance. Also, their young are typically referred to as hatchlings, is what?")
if answer.lower() == "troglodyte":
    print('Light Work Babbeehhh!')
    score += 1
else:
    print("Actually apply yourself worm")

# Question 2
answer = input("In Darwinian terms a person deemed 'least fit to reproduce', manifested in social terms as someone unable to copulate due to the absence of even a single willing partner. More typically male than female. Hangs around on internet forums generally blaming females for this undesirable condition.")
if answer.lower() == "incel":
    print('Light Work Babbeehhh!')
    score += 1
else:
    print("Actually apply yourself worm")

# Question 3
answer = input("One whom wears band shirts daily, shaves monthly, and bathes never. Often smelling of cheetos, Mountain Dew, and depression, is what?")
if answer.lower() == "neckbeard":
    print('Light Work Babbeehhh!')
    score += 1
else:
    print("Actually apply yourself worm")

# Question 4
# answer = input("A lower-functioning subspecies cave-dwelling humanoid that usually inhabits subterranean dwellings, and enjoys frequenting Wal-Mart. They tend to chiefly subsist on some form of government/taxpayer assistance. Also, their young are typically referred to as hatchlings, is what?")
# if answer.lower() == "troglodyte":
#     print('Light Work Babbeehhh!')
#     score += 1
# else:
#     print("Actually apply yourself worm")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%.")