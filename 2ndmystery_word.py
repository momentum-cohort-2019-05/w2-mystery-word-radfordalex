word = "blob"
#TODO import words from file

def play_game():
    guesses = []
    count = 0
    while count < 8:
        guess = input("guess a letter")

        if guess in word:
            print("correct")
        else:
            print("incorrect. try again")
        count += 1
#TODO store the guesses in list
play_game()

def display_letter()
    if letter in word:
        return letter
    else return "_"
    
