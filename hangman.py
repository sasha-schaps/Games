import random

def get_word():
  """Returns a random word from a list."""
  words = ["python", "javascript", "programming", "computer", "science"]
  return random.choice(words)

def display_hangman(tries):
  """Displays the hangman figure based on remaining tries."""
  stages = [  # Final state: head, torso, both arms, and both legs
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
                """,
                # Head, torso, both arms, and one leg
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
                """,
                # Head, torso, and both arms
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
                """,
                # Head, torso, and one arm
                """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
                """,
                # Head and torso
                """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
                """,
                # Head
                """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                """,
                # Initial empty state
                """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
                """
  ]
  return stages[tries]

def play_hangman():
  """Main game logic."""
  word = get_word()
  word_letters = set(word)  # Letters in the word
  alphabet = set(chr(x) for x in range(97, 123))  # All lowercase letters
  used_letters = set()  # What the user has guessed

  tries = 6  # Number of incorrect tries allowed

  # Get user input
  while len(word_letters) > 0 and tries > 0:
    # Letters used
    print('You have used these letters: ', ' '.join(used_letters))

    # Current word (e.g. "p - t - o n")
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print(display_hangman(tries))
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').lower()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
        print('')

      else:
        tries -= 1  # Takes away a life if wrong
        print('Letter is not in word.')

    elif user_letter in used_letters:
      print('You have already used that character. Please try again.')

    else:
      print('Invalid character. Please try again.')

  # Gets here when len(word_letters) == 0 OR tries == 0
  if tries == 0:
    print(display_hangman(tries))
    print('You died, sorry. The word was', word)
  else:
    print('You guessed the word', word, '!!')

if __name__ == "__main__":
  play_hangman()
