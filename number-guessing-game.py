import random

low = int(input("Enter lower bound:"))
high = int(input("Enter upper bound:"))

random_number = random.randint(low, high)

print(f"you have 7 chances to guess number between {low} and {high}. Lets start")

chances = 7
gc = 0

while gc < chances:
    gc += 1
    guess = int(input("Enter you guess number here:"))

    if guess == random_number:
        print(f"Congratutions! you have guess the number {random_number} in you {gc} try!")
        break
  
    elif gc == chances:
        print(f"Your chances are over. The random number is {random_number}.Better luck next time")

    elif guess > random_number:
        print("Your guess is too high.")
    elif guess < random_number:
        print("Your guess is too low")

                        