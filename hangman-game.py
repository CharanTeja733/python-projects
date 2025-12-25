""" Hangman game """
import random

FRUITS = """apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon"""

fruits = FRUITS.split()
print(fruits)

word = random.choice(fruits).lower()

if __name__ == "__main__" :
    try:
        name = input("What's your name?")
        print("Good luck! ", name)

        print("Game Starts! Guess the word")

        chances = len(word) + 2
        guessed_letters = set()

        #blank character for letters in word
        for _ in word:
            print("_", end= ' ')
        print()    
    
        while chances > 0:
            guess = input("Enter your guess:").lower()

            if not guess.isalpha():
                print("Enter only Letters")
                continue
            elif len(guess) != 1:
                print("Enter only one letter")
                continue
            elif guess in guessed_letters:
                print("you already guessed this letter")
                continue    
            
            if guess in word:
                guessed_letters.add(guess)
            else:
                chances -= 1
                print("wrong guess!")
                print("you have {} chances left".format(chances))

            for ch in word:
                print(ch if ch in guessed_letters else "_", end=" ")        

            print()        
                    
            if guessed_letters == set(word):
                print("You won")
                break

            if chances <= 0:
                print("You lost")
                print("The word is {}".format(word))
                print("Try Again!")    

    except (KeyboardInterrupt, EOFError):
        print("\nTry Again! Bye")
        exit()