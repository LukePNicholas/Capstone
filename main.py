import random

with open('Word.py') as f:
    wordlist = f.readlines()


def get_random_word():
    """Chooses a random word from the word list and returns it."""
    return random.choice(wordlist).lower().strip()


def get_completion(word, guessed):
    """Shows letters user guessed correctly, and shows _ for guessed letters."""
    return ''.join([letter if letter in guessed else '_' for letter in word])


def is_solved(word, guessed):
    """Checks if all letters in word have been guessed."""
    return len([letter for letter in word if letter not in guessed]) == 0


name = input('Please enter your name: ')
print(f"Welcome to Hangman, {name}!")


def hangman():
    """Gives user six tries to guess letters in the random word. If the letter they guess is incorrect,
     it subtracts a try, shows the next stage of the_man, and prompts them to input another letter until
     they either guess the word correctly or run out of tries."""
    word = get_random_word()
    guessed = []
    tries = 6
    while True:
        the_man(tries)
        print(get_completion(word, guessed))
        guess = input('Enter a letter: ').lower()
        if not guess.isalpha():
            print('You must enter a valid character.')
            continue
        if len(guess) != 1:
            print('You must guess exactly one letter.')
            continue
        if guess in guessed:
            print("You already guessed that letter!")
            continue
        guessed.append(guess)
        if is_solved(word, guessed):
            print(f'Congratulations, {name}! You guessed the word {word}.')
            return
        elif guess in word:
            print("Yes! Guess again.")
        elif guess not in word:
            tries -= 1
            print("Wrong letter! You have", tries, 'tries left.')
        if tries == 0:
            print(f"You ran out of guesses! The word was {word}.")
            the_man(tries)
            return


def the_man(tries):
    """Prints the current step of the hangman, and prints the next step of the hangman
    when a guess is incorrect."""
    stages = ['''
       ------    
       |    |
       |    0
       |  / | \\
       |   / \\
       |
    =======''',
              '''
       ------
       |    | 
       |    0
       |  / | \\
       |   /
       |
    =======''',
              '''
       ------
       |    |
       |    0
       |  / | \\
       |    
       |
    =======''',
              '''
       ------
       |    |
       |    0
       |  / | 
       |
       |
    =======''',
              '''
       ------
       |    |
       |    0
       |    |
       |
       |
    =======''',
              '''
       ------
       |    |
       |    0
       |   
       |   
       | 
    =======''',
              '''
       ------
       |    |
       |
       |
       | 
       | 
    =======''']
    print(stages[tries])


play_again = True
while play_again:
    hangman()
    response = ""
    while response != 'y' and response != 'n':
        response = input('Would you like to play again? Y/N ').lower()
        if response == 'n':
            print('Thank you for playing!')
            play_again = False
        elif response != 'y':
            print("Please choose y or n")
