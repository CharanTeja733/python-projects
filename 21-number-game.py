import random

abc = []

def player_move():
    flag = 0

    try:
        while flag == 0:
            try:
                k = int(input("Your turn.\nEnter your number in between 1 , 2 and 3:"))
            except ValueError:
                print("not valid input")
                continue
            if k not in [1, 2, 3]:
                print("Please enter only 1 or  2 or 3")
                continue

            flag = 1

            for _ in range(k):
                num = int(input(">"))

                if len(abc) == 0 and num != 1 or len(abc) > 0 and num != abc[-1] + 1:
                    print("wrong entry! you are disqualified")
                    return 1

                abc.append(num)

                if len(abc) >= 21: 
                    print("You lost! Try again")
                    return 1 
            
            print(abc)

    except (KeyboardInterrupt, EOFError):
        print("ok bye! Try again")
        return 1
    return 0

def computer_move():
    num = random.randint(1, 3)
    print(f"computer number is {num}")

    last_num = 0
    if len(abc) != 0:
        last_num = abc[-1]

    for k in range(1, num + 1):
        abc.append(last_num + k)
    
    print(abc)
    if len(abc) >= 21:
        print("You won the game")
   
def start():
    flag = 1
    try:
        while flag:
            flag = 0
            pos = input("Want to play first or second(F / S):")
            if pos != "F" and pos != "S":
                print("Enter only F or S")
                flag = 1

        if pos == "F" and player_move():
            return

        while len(abc) < 21:
            computer_move()
            if len(abc) >= 21:
                return
            if player_move():
                return
    except (KeyboardInterrupt, EOFError):
        print("ok bye! Try again")
        exit()     
    

if __name__ == "__main__":
    while True:
        print("21-number-game!")
        try:
            ans = input("Are you want to play the game:(y/n)?").lower()
            if ans == "y":
                start()
                break
            elif ans == "n":
                print("ok bye! try again")
                break
            else:
                print("enter only y / n") 
                continue 
        except (KeyboardInterrupt, EOFError):
            print("ok bye! Try again")
            exit()