"""
============================================================
============================================================
HANGMAN GAME
============================================================
============================================================

DOC:

============================================================
FUNC hangman
We define a funciton hangman that takes a param 'word';
The param 'word' is the word player 2 has to guess;
============================================================
VAR "word"
- PARAM of FUNC hangman;
- variable holds the correct word;
- the word player 2 has to guess to win;
============================================================
VAR "wrong"
- keep track of player 2's incorrect guesses;
============================================================
VAR "stages"
- is a list of strings;
- when python prints each stage in the list on a new line,
a picture of a hangman forms;

============================================================
VAR "remaning_letters"
- is a list containing each character in the VAR word;
- it keeps track of each letters that are left to guess;

============================================================
VAR "board"
- is a list of strings;
- used to keep track of the game board you display to player
2;
- this code populates the board list with an underscore for
every character in a variable word;

============================================================
VAR "win"
- starts a false, to keep track whether player 2 has one the
game yet;

============================================================

"""

import random

#============================================================
#Implement a modification so that a word is selected randomly
#from a list.
#============================================================
words_list = ["cat","dog","tree","sun","moon","rock","water","fire","air"]
r_word = random.randint(0,8)
word = words_list[r_word]
#============================================================

def hangman(word):
    
    wrong = 0
    stages = ["",              
             " _________      ",
             "|   /    |      ",
             "|  /     |      ",
             "| /    (0_o)    ",
             "|/      /|\     ",
             "|      / | \    ",
             "|       / \     ",
             "|      /   \    ",
             "|               ",
             "|\              ",
             "|_============= "
              ]
    remaning_letters = list(word)
    board = ["__"] * len(word)
    word_size = str(len(word))
    win = False


#============================================================
#1.
#Game starts here
#============================================================

    print("====================")
    print(" Welcome to Hangman")
    print("====================")


#============================================================
#2.
#A loop that keeps the game going.
#Continues as long as the VAR long is less than the length
#of the VAR stages LIS - 1.
#Game continueas until player 2 has guess more wrong letters
#than the number of string elements it takes to create the
#hangman.
#VAR char grabs input from player 2.
#============================================================


    while wrong < len(stages) - 1:
        print("\n")
        print("The word has "+word_size+" letters")
        print("=======================")
        msg = "Guess a letter: "
        char = input(msg)

#============================================================
#3.
#If does:
#- Check to to see if player 2 guessed correctly and update VAR
#board.
#- VAR cind checks the index of the correct char in vVAR
#remaning_letters. And updates VAR board by replacing the
#underscore with the letter guessed and replaces the guessed
#letter with a $ so that the guessed letter is no longer in
#the VAR remaining_letters.
#Else does:
#-If the guess is incorect, VAR wrong is incremented by 1.
#============================================================

        if char in remaning_letters:
            cind = remaning_letters.index(char)
            board[cind] = char
            remaning_letters[cind] = '$'
            print("\n")
            print("You found the letter: {}! :D ".format(char))
        else:
            print("\n")
            print("Incorrect letter!")
            print("The letter: {}, is not the word. :(".format(char))
            wrong += 1

#============================================================
#4.
#Prints out the board so that player 2 can make the next guess.
#============================================================

        print((" ".join(board)))
        e = wrong + 1
        print("\n=======================")
        print("The Hangman:")
        print("\n".join(stages[0: e]))
        wrong_rem = len(stages) - wrong
        print("\n")
        print("==============================================")
        print("Incorrect answers left: " + str(wrong_rem))
        print("==============================================")
        if "__" not in board:
              print("You win!")
              print(" ".join(board))
              win = True
              break
    if not win:
              print("\n".join(stages[0: wrong]))
              print("You lose! The correct word was: {}.".format(word))

    
hangman(word)
