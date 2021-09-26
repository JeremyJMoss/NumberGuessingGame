import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
randomNum = random.randint(1, 101);
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  attempts = 10
else:
  attempts = 5
game_over = False
while game_over == False:
  print(f"You have {attempts} attempts to guess the number")
  guess = int(input("Make a guess: "))
  attempts -= 1
  if guess < 1 or guess > 100:
    print("Invalid guess.")
  elif guess == randomNum:
    print(f"You got it! The number was {randomNum}!")
    game_over = True
  elif guess > randomNum:
    print("Too high.")
  else:
    print("Too low.")
  if game_over == False:
    if attempts == 0:
      game_over = True
      print("You've run out of guesses, You lose.")
    else:
      print("Guess again.")