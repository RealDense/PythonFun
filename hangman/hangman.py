from bs4 import BeautifulSoup
import requests

hangman = ['  ____  \n |    | \n |       \n |       \n |       \n |       \n_|______',
           '  ____  \n |    | \n |    O  \n |       \n |       \n |       \n_|______',
           '  ____  \n |    | \n |    O  \n |    |  \n |    |  \n |       \n_|______',
           '  ____  \n |    | \n |    O  \n |   /|  \n |    |  \n |       \n_|______',
           '  ____  \n |    | \n |    O  \n |   /|\ \n |    |  \n |       \n_|______',
           '  ____  \n |    | \n |    O  \n |   /|\ \n |    |  \n |   /   \n_|______',
           '  ____  \n |    | \n |    O  \n |   /|\ \n |    |  \n |   / \ \n_|______']


def find_all(string, letter):
    indexes = []
    previous_index = string.find(letter)
    indexes.append(previous_index)
    while previous_index >= 0:
        previous_index = string.find(letter, previous_index+1)
        if previous_index >= 0:
            indexes.append(previous_index)
    return indexes


def replace_blanks(blanks_string, indexes, char):
    return "".join([char if i in indexes else ch for i, ch in enumerate(blanks_string)])

#print(find_all("alex was here",'e'))


keep_playing = True
current_guess = ""

while keep_playing:
    site = requests.get('https://randomword.com')
    soup = BeautifulSoup(site.text, 'html.parser')
    word = soup.find('div', id='random_word').text
    definition = soup.find('div', id='random_word_definition').text
    letters = set([i for i in word])
    blanks = '_'*len(word)
    # print(word, letters, blanks, definition)
    guesses = []
    counter = 0
    still_alive = True
    while still_alive:
        guess = ''
        print('Previous Guesses: ', guesses)
        print(hangman[counter])
        print(blanks)
        if blanks == word:
            print("\n\nCongratulations! YOU WON!!!\n", '\n\nWord: ',
                  word, '\nDefition: ', definition, '\n\n')
            still_alive = False
            break
        if counter >= len(hangman)-1:
            print('\n\nYOU LOSE!\n\nWord: ', word,
                  '\n\nDefition: ', definition)
            still_alive = False
            break
        while True:
            if len(guess) == 0:
                if len(current_guess) == 0:
                    guess = input('What is your guess? ')
                    if len(guess) > 1:
                        current_guess = guess[1:]
                        guess = guess[0:1]
                else:
                    guess = current_guess[0]
                    current_guess = current_guess[1:]
            if len(guess) > 1 or len(guess) <= 0:
                print('Please only type one letter. ')
            elif guess in guesses:
                print('Previous Guesses: ', guesses)
                print("You've already used that letter. Please try another ")
                guess = ''
            else:
                break
        guesses.append(guess)
        if guess in letters:
            print ('Good Guess')
            blanks = replace_blanks(blanks, find_all(word, guess), guess)
        else:
            print('Oops, you guessed wrong.')
            counter += 1
            print(counter)
    if input('Would you like to play again? y/n ').lower() != 'y':
        keep_playing = False

find_all(word, 'a')
