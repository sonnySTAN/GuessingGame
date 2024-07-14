##Allison Stankov CIS261 Gussing Game##
print("GUESS THE NUMBER")

playagain="y"
while playagain.lower() == "y":
    limit = int(input("\nEnter the upper limit:  "))
    import random
    num = random.randint(1,int(limit))
    print(f"I'm thinking of a number between 1 and {limit}.")
    guess = int(input("\nWhat number am I thinking of?  "))
    count = 0
    while True:
        if int(guess)>int(num):
            print("Lower!")
            guess = int(input("\nTry again. What number am I thinking of?  "))
            count+=1
        elif int(guess)<int(num):
            print("Higher!")
            guess = int(input("\nTry again. What number am I thinking of?  "))
            count+=1
        elif int(guess)==int(num):
            print("That's right!")
            count+=1
            print(f"You got it in {count} tries.")
            playagain = input("\nWould you like to play again? Enter y or n:  ")
            while playagain.lower() not in ["y","n"]:
                playagain = input("\nWould you like to play again? Enter y or n:  ")
            break
else:
    print("Thanks for playing!")

