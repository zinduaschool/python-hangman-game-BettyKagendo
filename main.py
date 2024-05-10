import random

#create a list of words
hangman_words = ['whizzing', 'fishhook', 'beekeper', 'rhythm', 'stronghold']

def get_random_word():
    #choose a random word from the list
    word = random.choice(hangman_words)
    return word
print (get_random_word())


















