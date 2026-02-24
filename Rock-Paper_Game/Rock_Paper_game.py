import random

a = ["Rock" , "Paper" , "Scissor"]

print("Welcome! Lets Start the Game \nRock, Paper, Scissors")

Round = 0

while True:
    user = input("Enter a word: ")
    b = random.choice(a)
    print(f"Computer Word:", b)

    if user=="Rock":
        if b==a[1]:
            print("You Lose")
        elif b==a[2]:
            print("you Won")
        else:
            print("Tie")

    if user=="Paper":
        if b==a[0]:
            print("You Win")
        elif b==a[2]:
            print("you Lose")
        else:
            print("Tie")

    if user=="Scissor":
        if b==a[0]:
            print("You Lose")
        elif b==a[1]:
            print("you Won")
        else:
            print("Tie")
    Round += 1 
    
    print(f"Round = {Round} \n"  )
    










