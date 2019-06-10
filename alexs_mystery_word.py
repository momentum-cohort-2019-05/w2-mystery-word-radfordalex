def display_letter(letter, correct_letters):
    if letter in correct_letters:
        return letter
    else:
        return "_"

def print_guess_letters(correct_letters, word):
    display_list = []
    for letter in word:
        display_letter(letter, correct_letters)
        print(display_list)

def user_guesses(correct_letters):

    guess = input("guess letter ")

    if guess in word:
        print("correct")
        correct_letters.append(guess)
        print_guess_letters(correct_letters, word)
    else:
        print("incorrect")

correct_letters = []
word = "turtle"

while len(correct_letters) < len(word):
    user_guesses(correct_letters)





        