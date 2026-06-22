secret = 12
lives = 5


while lives > 0:
    guess = int(input("Guess the number"))

    if guess == secret:
         print("You Win")
        
    difference = guess - secret 
    if difference < 0:
         difference = -difference
    if difference <= 4:
        print("Ice cold")
    elif difference  <= 6:
        print("cold")
    elif difference  <= 10:
        print("Warm")
    else: 
        print("Hot")

