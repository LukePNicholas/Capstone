import random

with open('Word.py') as f:
    wordlist = f.readlines()


def get_random_word():
    return random.choice(wordlist).lower().strip()


def get_completion(word, guessed):
    return ''.join([letter if letter in guessed else '_' for letter in word])


def is_solved(word, guessed):
    return len([letter for letter in word if letter not in guessed]) == 0


print("Welcome to hangman!")
input('Please enter your name: ')


def hangman():
    word = get_random_word()
    guessed = []
    tries = 6
    while True:
        the_man(tries)
        print(get_completion(word, guessed))
        guess = input('Enter a letter: ').lower()
        if len(guess) != 1:
            print('You must guess exactly one letter')
            continue
        if guess in guessed:
            print("You already guessed that letter!")
            continue
        guessed.append(guess)
        if is_solved(word, guessed):
            print('Congratulations! You guessed the word', word)
            return
        elif guess in word:
            print("Yes!, guess again")
        elif guess not in word:
            tries -= 1
            print("Wrong letter! You have", tries, 'tries left')
        if tries == 0:
            print("You ran out of guesses! The word was", word)
            the_man(tries)
            return


def the_man(tries):
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
        response = input('Play again? Y/N ').lower()
        if response == 'n':
            play_again = False
        elif response != 'y':
            print("Please choose y or n")
