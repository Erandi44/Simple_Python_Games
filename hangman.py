"""
Hangman Game : This program is a version of the classic letter guessing game called Hangman. You are shown a number of letter letters that match a word and you have to guess what these letters are to reveal the hidden word. You guess by picking letters from the list displayed. If you pick a letter that is in the word, a letter is revealed from the blank letters; however, if you pick a letter that is not in the word, then a stickman starts slowly drawn. With each wrong letter guess, the man is drawn more and more. After 6 w®ong attempts, he is hung and the game is lost.If you can reveal all the letters in the word before the man is hung then you are successful and the full word is revealed.

Author : Erandika Karunaratne
Date : 2022-07-08

"""
    
import random
from words import words
import string


words = [word.upper() for word in words ]


def select_word(words):
    random_word = random.sample(words,1) 
    
    # check vaildity of the word. Words with "_" or " " are invalid.
    while ("_" or " ") in random_word:
        random_word = random.sample(words,1)

    word = ' '.join(map(str,random_word))
    #print(word)  
    return word



def check_word(word):
    length = len(word)#length of the word
    let_list = list(word) #list containg the letteres of the selected word
    #print(let_list)
    all_letters = list(string.ascii_uppercase)#All letters from alphabet

    user_string ="" #String constructed by user input
    used_letters =[]#Letters that user has used so far   
    no_lives =6 #person will be hanged after 6 wrong attempts
    remaining_lett = all_letters # remaining letters in the alphabet
    new_string=[] #list created by user input
    for let in let_list:
        new_string.append("_")
      
    print(f"You need to guess a word with {length} letters.") 
    
    while user_string!=word:
        print("\n")
        print("Pick a letter from the following list")
        print(remaining_lett)
    
        
        user = input("Guess a letter:")
        user = user.upper()
        
        remaining_lett = [let for let in all_letters if let not in used_letters]    
        
        if str(user) in remaining_lett: 
            used_letters.append(user)          
            #print(used_letters) 
        
            if user in let_list:
                i=0
                for let in let_list:
                    if let_list[i]==user:
                        new_string[i] = user
                    i =i+1           
                print(new_string)
                user_string = ''.join(map(str,new_string))
                     
            else:
                no_lives = no_lives-1
                print(new_string)
                print("Wrong guess")
                print(f"You have {no_lives} lives remaining")
                used_letters.append(user)
                if no_lives == 0:
                    print("Sorry, you've lost!")
                    return
                    
        else:
            print("You've already used this leter. Try another.")
            continue
            
    print(user_string)
    print("Yay! You've won.")
    return




def main():
    response = "Y"
    
    while response == "Y":
        word = select_word(words)
        check_word(word)
        response = input("Do you want to play again (Y/N)?:")
        response = response.upper()
              

if __name__ == "__main__":
    main()







    
