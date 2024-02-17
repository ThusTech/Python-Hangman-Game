from patterns import Pattern
from enum import *


def encapsulate(word):
    filterWord = word.replace(" ","").upper()
    encapsulatedWord = ""

    for letter in filterWord:
        encapsulatedWord += "_"
        
    return encapsulatedWord,filterWord

def gameLoop(lives,encapsulatedSet):
    guessedWord = list(encapsulatedSet[0])
    word = encapsulatedSet[1]
    foundLetter = False

    while lives > 0:
        print("Word : "+ " ".join(guessedWord))
        letter = input("Guess the letter: ").upper()

        if not letterValidate(letter):
            print("Invalid Charecter")
            continue

        for index, actualLetter in enumerate(word):
            if letter == actualLetter:
                guessedWord[index] = letter
                foundLetter = True
        
        if not foundLetter:
            lives-=1

        foundLetter = False
        pattern(lives)

        if lives == 0:
            print("GAME OVER YOU LOOSE")
        elif word == "".join(guessedWord):
            print("GAME OVER YOU WIN")
            break

           
def letterValidate(letter: str): 
    return letter.isalpha()

def pattern(lives):
    patterns = list(Pattern)
    index = (len(patterns)-1) - lives

    print(patterns[index].value)

def main():
    # Maximum number of lives
    LIVES = 5
    word = "South Africa"

    
    print("""
    -------------------------
    ||   Hint: A Country   ||
    ------------------------=\n""")

    pattern(LIVES)

    gameLoop(LIVES, encapsulate(word))


if __name__ == '__main__':
    main()