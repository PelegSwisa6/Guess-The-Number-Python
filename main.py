#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random


def Game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")

    def easy():
        answer = random.randint(0, 100)
        print(f"Psst the answer is {answer}")
        lives = 10

        for i in range(0, lives):
            print(
                f"You have {lives - i} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if guess == answer:
                print("You got it")
                break
            if guess > answer:
                print("Too High")
            if guess < answer:
                print("Too Low")
            if i == lives - 1 and guess != answer:
                print("The attempts are over, you have lost the game!")

    def hard():
        answer = random.randint(0, 100)
        print(f"Psst the answer is {answer}")
        lives = 5

        for i in range(0, lives):
            print(
                f"You have {lives - i} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if guess == answer:
                print("You got it")
                break
            if guess > answer:
                print("Too High")
            if guess < answer:
                print("Too Low")
            if i == lives - 1 and guess != answer:
                print("The attempts are over, you have lost the game!")

    if difficulty == "hard":
        hard()
    else:
        easy()


Game()
play = input("Want play more game ? Y/N ")

while (play == 'y'):
    Game()
    play = input("Want play more game ? y/n ")

print("Thank you See ya!")

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
