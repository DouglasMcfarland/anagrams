import string
import random
import sys

# load_words() takes a list of words from a file and returns
# a list one element for each line in the file. The scrabble word list
# works best but it doesn't include words longer than 8 characters.
def load_words():
    words = []
    with open('words.txt') as word_file:
        valid_words = list(word_file.read().split())
    for i in valid_words:
        words.append(i.lower())
    return words

def load_words_two():
    words = []
    with open('gauragram.txt') as word_file:
        valid_words = list(word_file.read().split())
    for i in valid_words:
        words.append(i.lower())
    return words


# words_of_length(num, word_list) takes an integer and a list of strings 
# and returns a list including only strings of length num 
def words_of_length(num, word_list):
    word_lengthx = []
    for i in word_list:
        if len(i) == num:
            word_lengthx.append(i)
    return word_lengthx

# word_matches (word, word_list) takes a word and a word list and returns all 
# the anagrams in the list including word. It is the brains of the operation.
def word_matches (word, word_list):
    key_list = []
    alpha_chars_match = "".join(sorted(word)) 
    for i in word_list:
        if alpha_chars_match == "".join(sorted(i)) and i != word:
            key_list.append(i)
    return key_list

# anagram_solver (word, word_list) stitches together two functions
# takes a word and a list of words and makes a shorter list of only words of the length of the # # word and then checks the shorter list for anagrams. It returns all matches.
def anagram_solver (word, word_list):
    x = len(word)
    short_list = words_of_length (x, word_list)
    return word_matches (word, short_list)

# chooses a random word from a list
def anagram_picker (word_list):
    pick = random.choice(word_list)
    return pick

# takes a word list of words and a number of solutions and returns True if the word
# as more solutions than the number. straight greater than is preferable here
# because that is how many solutions there are because the list includes the word 
# that it is checking.
def good_or_bad (word, word_list, num):
    a_list = anagram_solver(word, word_list)
    if len(a_list) > num:
        return True
    else:
        return False

# This makes a list of good anagram words. If run with num set to 4 it will make a list
# of anagrams that all have at least 4 solutions. It takes a long time to run. It was used to
# make gauragram.txt and is here for reference.
def make_list (word_list):
    internal_list = []
    for i in word_list:
        if good_or_bad(i, word_list, num):
            internal_list.append(i)
            print(i)
    return internal_list

def main ():
    number_rounds = 3
    score = 0
    correct_guesses = []
    print("Welcome to Anagrams!")
    print("You may play a single scored game, or a scored round of three with highscores!\n")
    a = input("Enter 1 for Quick Play, 2 for Scored Round, or 3 to quit: ")
    if a == '1':
        guesses = []
        words = load_words()
        puzzles = load_words_two()
        puzzle = random.choice(puzzles)
        solves = anagram_solver(puzzle, words)
        num_solutions = len(solves)
        print("Your word is",puzzle)
        print("The number of possible anagrams is ",num_solutions)
        guess = input("Enter all the anagrams you can think of: ")
        guesses = guess.split()
        for i in guesses:
            if i in solves:
                score += 1
                correct_guesses.append(i)
        print("You got ",score," correct")
        print("You found the following anagrams, ", correct_guesses)
        print("All the solutions to this puzzle are, ",solves)
    
    elif a == '2':
        for i in range(number_rounds):
            correct_guesses = []
            guesses = []
            words = load_words()
            puzzles = load_words_two()
            puzzle = random.choice(puzzles)
            solves = anagram_solver(puzzle, words)
            num_solutions = len(solves)
            print("Your word is",puzzle)
            print("The number of possible anagrams is ",num_solutions)
            guess = input("Enter all the anagrams you can think of: ")
            guesses = guess.split()
            for i in guesses:
                if i in solves:
                    score += 1
                    correct_guesses.append(i)
            print("Your score is ",score)
            print("You found the following anagrams, ", correct_guesses)
            print("All the solutions to this puzzle are, ",solves,"\n")
        print("Congrats your final score is",score)       
        
            


        
    else:
        print("Thanks, Come again soon.")
        sys.exit()
    

if __name__ == "__main__":
    main()
