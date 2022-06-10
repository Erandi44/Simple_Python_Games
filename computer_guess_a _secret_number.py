# Computer guess a secret number that user have chosen.

import random
    
def computer_guess():
    print("You can specify a range for the number you've picked.")
    low = int(input("Lower end of the range: "))
    high = int(input("Higher end of the range: "))
    response = ""
    
    while response != "C":
        guess = random.randint(low,high)
        print(guess)
        response = input("Is the guess too high(H), too low(L) or correct(C): ")
        
        if response =="L":
            low = guess
            continue
        elif response == "H":
            high = guess
            continue
        else:
            print(f"Yay!The computer predicts your number {guess} correctly!")
    
def main():
    computer_guess()
    
if __name__ == "__main__":
    main()
