#  Overview

This is a Password Guessing Game built using Python.
The game allows users to select a difficulty level and guess a randomly chosen word.
After each incorrect guess, the program provides helpful hints by revealing correctly positioned letters.
The game continues until the user correctly guesses the secret word.

#  Features

-Three difficulty levels: Easy, Medium, Hard
-Random word selection using Python’s random module
-Unlimited attempts until correct guess
-Attempt counter to track performance
-Word hint system (reveals correct letters in correct positions)
-Input validation with default difficulty setting

#  How the Game Works

-The user chooses a difficulty level.
-The program randomly selects a word from the selected list.
-The user starts guessing the word.
-If the guess is incorrect:
-The program shows a hint.
-Correct letters in correct positions are displayed.
-Incorrect letters are replaced with _.
-The game continues until the correct word is guessed.
-The total number of attempts is displayed.

#  Concepts

Lists                                      – Used to store multiple words under different difficulty levels (easy, medium, hard).
Conditional Statements (`if-elif-else`)    – Used to select the difficulty level and assign the appropriate word list based on user input.
Loops (`while` and nested `for`)           – The `while` loop keeps the game running until the correct guess, and the nested `for` loop checks each letter to generate hints.
String Indexing                            – Used to access and compare individual letters of the guessed word and the secret word using positions like `word[i]`.
User Input Handling                        – The `input()` function collects user guesses and difficulty choices, ensuring interactive gameplay.
Boolean Logic                              – Conditions like `guess == secret` and `i < len(guess)` evaluate True or False to control program flow.
Random Module Usage                        – The `random.choice()` function selects a random word from the chosen difficulty list.
Variables                                  – Used to store important data such as the secret word, user guess, attempts counter, and generated hints.

