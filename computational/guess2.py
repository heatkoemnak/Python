import random as rand
compnumber = rand.randint(1, 2)
usernumber = int(input("Choose a number between 1 and 100. You'll get 5 guesses or you lose! "))

if compnumber == usernumber:
    #if the number user input is the same computing's computer
    print("You win!")
else:
    #if not the same
    print("You lose!")