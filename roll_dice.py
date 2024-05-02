import random
roll = random.randint(1,6)
guess = int(input('Guess the dice roll:'))
if guess == roll:
    print("Correct they rolled" + str(roll))
else:
    print("wrong they rolled" + str(roll))

