secret = 12
lives = 5

while lives > 0:
    guess = int(input("Guess the number:"))

    if guess == secret: 
        print("You win")
        break 

    difference = guess - secret
    if difference < 0:
        difference = -difference 
    if difference <= 2:
        print("Hot")
    elif difference <= 4:
        print("Warm")
    elif difference <= 7:
        print("Cold")
    else:
        print("Ice Cold")
    lives = lives - 1
    if lives == 0:
        print("Game over!")
        print("The secret number was:", secret)