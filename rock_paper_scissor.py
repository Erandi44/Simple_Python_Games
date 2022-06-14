# ------------------------------Rock Paper Scissor Game-------------------------------------------------------
# The rules are:
#  * Rock smashes scissors.
#  * Paper covers rock.
#  * Scissors cut paper.
# ------------------------------------------------------------------------------------------------------------

import random

rock = 0
paper = 1
scissor = 2
choices = {"Rock":0, "Paper":1, "Scissor":2}



def action(choices):
    user = int(input(f"Pick your choice, Rock(0), Paper(1), or scissor(2):  "))
    
    if user not in [0,1,2]:
        print("Invalid input. Try again")
        user = int(input(f"Pick your choice, Rock(0), Paper(1), or scissor(2):  "))
        
    computer = random.choice(list(choices.values()))
    print (f"Computer have chosen:{computer}") 
    
    winner(user,computer)
    repeat()
    

            
def winner(user, computer):
    #1>0, 0>2, 2>1
    if (computer==1 and user==2) or (computer==2 and user==0) or (computer==0 and user==1):  
        print("You've won")
    elif computer ==user:
            print("That's a tie")   
    else:
        print("You've lost")
            

def repeat(): 
    response = input("Would you like to play another round(Y/N)? ")
    
    if response.lower() == "y":
        action(choices)
    else:
        quit()
    
    

        
        
def main ():
    action(choices)
           
    
    
if __name__ == "__main__":
    main()
           
    
    






