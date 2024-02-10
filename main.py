#Importing random to later return one randomly chosen Pokémon
import random

#This function prints the games rules along with the character indicators
def game_rules():
  print(
    """\nPokéWordle is a Pokémon-themed word guessing game. You have 6 tries to guess the 5 letter name of the Pokémon. Each guess must be a valid word.\n
Guess Progression: "✅❌❌✅➕"\n
✅ - Indicates that the letter at that position was guessed correctly.
➕ - Indicates that the letter at that position is in the hidden word, but in a different position.
❌ - Indicates that the letter at that position is wrong, and isn't in the hidden word.""")

#This function reads the text file then randomly chooses and returns one name
def get_pokemon():
  with open("pokemon.txt", "r") as pokemon:
    name = pokemon.readlines()
    return random.choice(name) #Using the random module, we can choose a name without having to write out all of the random logic.

#Once called, this function handles the display of the guesses and the indicators
def guesses(pokemon, user_guess):
  for char, word in zip(pokemon, user_guess):
    #If letter is in the answer and correct position
    if word in pokemon and word in char:
      print(word + " ✅")
    #If letter is in the answer, but not correct position
    elif word in pokemon:
      print(word + " ➕")
    else:
      print(word + " ❌")

#This function handles the main gameplay
def gameplay():
  continue_playing = True

  #This function runs at the end of the game to ask the user if they would like to play again or not
  def ask_play_again():
    play_again = input("Press Enter to play again or type 'quit' to exit: ").strip()
    if play_again.lower() == 'quit':
      continue_playing = False
    else:
      game_rules()
      gameplay()

  #Here we strip any whitespace and capitalize the correct answer
  correct_guess = (get_pokemon()).strip().capitalize()
  attempt = 6

  #This while loop runs as long as the user has attempts left and continue_playing is set to True
  while attempt > 0 and continue_playing:
    #Here we strip any whitespace and capitalize the users’ guess
    user_guess = str(input("\nGuess the Pokémon: ")).strip().capitalize()

    #If the guess is an alphabetical character and only 5 letters long, continue.
    if user_guess.isalpha() and len(user_guess) == 5:
      #Here we check first for the win condition
      if user_guess == correct_guess:
        guesses(correct_guess, user_guess)
        print("\nYou guessed the Pokémon correctly! Congrats! 🥳 🥳 🥳\n")
        attempt = 0
        ask_play_again()
      #Otherwise the user keeps guessing
      else:
        attempt -= 1
        print(f"You have {attempt} attempt(s) remaining... \n")
        guesses(correct_guess, user_guess)
        #Once the attempts reach zero, Game Over!
        if attempt == 0:
          print(f"\nGame over! 😭 😭 😭 Correct answer: {correct_guess}\n")
          ask_play_again()
    #This runs if the conditions for guess length and alphabet letters are not met
    else:
      print("\nPokémon names only consist of 5 alphabetical letters. Please guess again!")

#Start point of the entire py script
if __name__ == "__main__":
  game_rules()
  gameplay()