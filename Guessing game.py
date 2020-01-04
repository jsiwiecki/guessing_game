#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

#Computer player generates a random number within the range <1, 100> (inclusive).
def assign_rand_num(min_value,max_value):
    comp_number = random.randint(min_value,max_value)
    return comp_number

#Computer player asks the human player to guess the number. Human player provides the guess.

def ask_player(min_value, max_value):
    while True:
        player_number = input("Give an integer number between {} and {}".format(min_value, max_value))
        try:
            player_number = int(player_number)
            if player_number >= min_value and player_number <= max_value:
                return player_number
        except ValueError:
            print("It's not a number. Please put a number between {} and {}. Try again".format(min_value,max_value))
            continue
        else:
            print("It's not an integer number between {} and {}. Please try again".format(min_value,max_value))
            continue
            
#Computer player compares the numbers and provides a feedback for the human player 
#whether the given number was too low, too high or correct.
#The steps 2-4 are repeated until the human player gives the correct number.

def compare_user_comp(min_value, max_value):
    comp_number = assign_rand_num(min_value,max_value)
    player_number = None
    
    while comp_number != player_number:
        player_number = ask_player(min_value,max_value)
        if comp_number < player_number:
            print("Hint: Your number is too high. Try once more!")
            continue
        elif comp_number > player_number:
            print("Hint: Your number is too low. Try once more!")
            continue
    print("Congrats! That's the correct number")
    
def game():
    min_value = 1
    max_value = 100
    
    compare_user_comp(min_value, max_value)
    run()
    
def run():
    play = str.lower(input("Do you want to run a guesing game? (y/n)"))
    if play == 'y':
        game()
    elif play =='n': 
        print('Bye!')
    else:
        print('Please use only "y" or "n"')
        run()
        
if __name__ == '__main__': run() 

