import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
name = input("What is your name?")

print(f"Hi{name} Good Luck!")
print("Guess  the characters")
guesses = ""
turn = 12

while turn > 0:
  failed = 0
  
  for ch in word:
    if ch in guesses:
      print(ch)
    else:
      print("_")
      failed += 1  
  
  if failed == 0:
    print(f"you guessed correct! The word is {word}")
    break

  print()  
  guess = input("Guess the character:")  
  guesses += guess

  if guess not in word:
    turn -= 1
    print("wrong! \n guess, you have", + turn , "turn left")
  
  if turn == 0:
   print("You losses")




