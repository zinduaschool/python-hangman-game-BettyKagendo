#def play_hangman():
    #choosing a random word from the list
word = random.choice (hangman_words)

word_letters = set(word)

alphabet = set ('abcdefghijklmnopqrstuvwxyz')
used_letters = set()
print (word_letters)


def display_word (word):
    #create a list of dashes for each letter in the word to be guesssed
    word_display = ['_'] * len(word)
    print(' ,'.join(word_display)) #concatenates all the elements of word_display and separates them with spaces

#main game loop
def play_hangman():