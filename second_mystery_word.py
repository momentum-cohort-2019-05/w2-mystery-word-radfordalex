import random

with open ("words.txt") as file:
    words = file.readlines()
    words = [word.strip("\n") for word in words]
#TODO import words from file

def display_letter(letter, word):
    if letter in word:
        return letter
    else: 
        return "_"

def show_guessed_letters(correct_guesses, word):
    list_of_guesses = ""
    for letter in correct_guesses:
        list_of_guesses += display_letter(letter, word)
    return list_of_guesses


def play_game(words):
    correct_guesses = []
    word = random.choice(words)
    count = 0
    while count <= 8:
        print(word)
        guess = input("guess a letter ")
        
        if guess in word:             
            print(f"correct. you have {8-count} guesses left")
            correct_guesses.append(guess)
            list_of_guesses = show_guessed_letters(word, correct_guesses)
            print(list_of_guesses)
            if "_" not in list_of_guesses:
                print(f"YOU WIN!!!!! The word was {word} ")
                return
           
        else:
            print(f"incorrect. try again. you have {8-count} guesses left")
            count += 1
#TODO store the guesses in list
play_game(words)


