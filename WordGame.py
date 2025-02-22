#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for ch in word:
        if letter == ch:
            return True
    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    correctLetter = word[spot]
    if letter == correctLetter:
       return True
    else:
        return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = ""

    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot):
             feedback += myLetter.upper()
        elif inWord(myLetter, word):
            feedback += myLetter.lower()
        else:
            feedback += "*"

    return feedback    

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
   

    #User should get 6 guesses to guess
    for guessNum in range(1, 7):
        while True:
        #Ask user for their guess
            guess = input(f"Guess {guessNum}/6: ").strip().lower() 
        
            if len(guess) == 5 and guess.isalpha():
                break
            print("Invalid Guess! Enter 5 letter word.")

        feedback = rateGuess(guess, todayWord)
        print(feedback)

        if guess == todayWord:
            print("Winner Winner")
            return

    

    print(f"out of guesses! The correct word was {todayWord}")


if __name__ == '__main__':
    main()
