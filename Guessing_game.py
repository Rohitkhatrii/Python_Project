# importing random module
import random

# Making lists 
easy_words = ["salt" , "door" , "gate" , "key" , "man" ]
medium_words = ["python" , "Battle" , "shepherd" , "keyboard" , "utensil" ]
hard_words = ["nomenclature" , "government", "friendship" , "hospitality" , "direction"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: easy, medium or hard")

level = input("enter difficulty: ").lower()

# difficulty selection by user          # using conditional statements
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid input, Difficulty set to easy")       # accepting default input
    secret = random.choice(easy_words)

attempts = 0
print("Guess the secret word")

# Starting the Game
while True:
    guess=input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations!\n You Won with attempts: {attempts} ")
        break
    hint =""

    for i in range(len(secret)):             #  nested loop for inside while loop
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint: ", hint)

print("Game is Over")
            
    

    
