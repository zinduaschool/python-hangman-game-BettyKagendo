import random

#create a list of words
hangman_words = ['quorum', 'haphazard', 'strenghts', 'icebox', 'bookworm']

def get_random_word():
    #choose a random word from the list
    word = random.choice(hangman_words)
    return word
#print (get_random_word())


def display_word (word, correct_letters):
    #create a list of dashes for each letter in the word to be guesssed
    word_display = [' '.join([letter if letter in correct_letters else '_' for letter in word])]
    print(' '.join(word_display)) #concatenates all the elements of word_display and separates them with spaces

#defining the play game function
def play_hangman():
    word = get_random_word()
    word_letters = set(word)
    word_display = ['_'] * len(word)
    used_letters = set() #store the letters already guessed
    correct_letters = set()
    failed_attempts = 0
    max_failed_attempts = 6

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
                    display_word(word, correct_letters)
                    
                else:
                    failed_attempts += 1
                    print(f"Sorry, the letter '{user_input}' is not in the word.")
                    print (f"You have {max_failed_attempts- failed_attempts} attempts remaining ")

            if set(word) == correct_letters:
                    print (f"Congratulations! You have guessed the word '{word}")
                    break
            if failed_attempts == max_failed_attempts:
                print (f"You have ran out of attempts. The word was '{word}'. You lost")
                break


         except ValueError as err:
            print(err)

play_hangman()
             

























