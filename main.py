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
    print(' '.join(word_display)) #concatenates all the elements of word_display and separates them with spaces

#defining the play game function
def play_hangman():
    word = get_random_word()
    word_letters = set(word)
    word_display = ['_'] * len(word)
    used_letters = set() #store the letters already guessed
    correct_letters = set()

    while True:
         print(' '.join(word_display))
         user_input = input('Guess a letter: ').lower()

         try:
            if len(user_input) != 1:
                raise ValueError ('Please enter a single letter.')  
            elif user_input.isdigit():
                raise ValueError ('Letters only, please. No numbers allowed!')
            elif user_input in used_letters:
                raise ValueError (f"You have already guessed '{user_input}. Try a different letter.")
            else:
                used_letters.add(user_input)
                
                if user_input in word_letters:
                    correct_letters.add(user_input)
                    word_letters.remove(user_input)
                    print(f"Good guess! The letter ;{user_input} is in the word.")
                    word_display = [' '.join([letter if letter in correct_letters else '_' for letter in word])]

                    
                else:
                    print(f"Sorry, the letter '{user_input}' is not in the word.")

            if set(word) == correct_letters:
                    print (f"Congratulations! You have guessed the word '{word}")
                    break


         except ValueError as err:
            print(err)

play_hangman()
             

























