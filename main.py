import random
f = open(word.txt, 'r')
wordlist = f.read()




def hangman():
    word = random.choice(wordlist)
    guessed = []
    tries = 6
    input('Please enter your name: ')

    while tries > 0:
        for letter in word:
            if letter in guessed:
                print(letter)
            else:
                print("_")

        guess = input('Enter a letter: ').lower()
        guessed.append(guess)

        if guess not in word:
            tries -= 1
            print("Wrong letter! You have", tries, 'left')





    if tries == 0:
        print("You ran out of guesses! The word was", word)





theman = ['''
       ------    
       |    |
       |
       |
       |
       |
    =======''', '''
       ------
       |    | 
       |    0
       |
       |
       |
    =======''', '''
       ------
       |    |
       |    0
       |    |
       |
       |
    =======''', '''
       ------
       |    |
       |    0
       |   /|
       |
       |
    =======''', '''
       ------
       |    |
       |    0
       |   /|\
       |
       |
    =======''', '''
       ------
       |    |
       |    0
       |   /|\
       |   / 
       | 
    =======''', '''
       ------
       |    |
       |    0
       |   /|\
       |   / \
       | 
    =======''']