import random

#create a list of words
hangman_words = ['whizzing', 'fishhook', 'beekeper', 'rhythm', 'stronghold']

def get_random_word():
    #choose a random word from the list
    word = random.choice(hangman_words)
    return word
#print (get_random_word())


def display_word (word):
    #create a list of dashes for each letter in the word to be guesssed
    word_display = ['_'] * len(word)
    return word_display
    #print(' ,'.join(word_display)) #concatenates all the elements of word_display and separates them with spaces




















