from bs4 import BeautifulSoup
import requests
import keyboard

#allowed_letters = ['a', 'e', 't', 'b', 'd', 'l', 's', 'n']
#allowed_letters = ['a', 'd', 'e', 'h', 'i', 'l', 'n', 'r', 's', 't', 'y']
allowed_letters = ['n', 'o', 's', 't', 'r', 'i', 'l', 'a', 'e', 'd', 'c', 'y']

words = []


def allowed_word(word):
    for letter in word:
        # print(letter, end='')
        if(letter not in allowed_letters):
            return False
            # print('   not in', end='')
        # print('')
    return True


keep_playing = True
counter = 0

while (counter < 10000):
    site = requests.get('https://randomword.com')
    soup = BeautifulSoup(site.text, 'html.parser')
    word = soup.find('div', id='random_word').text
    definition = soup.find('div', id='random_word_definition').text
    # print(word, letters, blanks, definition)
    if allowed_word(word):
        if word not in words:
            words.append(word)
    counter += 1
    if(counter % 10 == 0):
        print(counter)
    if keyboard.is_pressed('t'):
        print(len(words))


for word in words:
    print(word)

print(len(words))
