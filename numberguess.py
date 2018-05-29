"""
*********************************************************************
* Project : POP1 (Practical Exam)
* Program name : q2.py
* Author : varunk01
* Purpose  : Attempts to solve the question 2 from the exam paper
* Date created : 28/05/2018
*
* Date           Author           Ver     Comment
* 28/05/2018     varunk01         0.1     Initial Version
**********************************************************************
Write a program for a number guessing game. The program generates a random
number between 0 and 99, and then asks the user to guess that number. For
each guess the program replies Correct, Too low, or Too high. If the number
is correct, the program prints the number of guesses it took. If not, the program
asks the user to guess again. For example:
Guess a number between 0 and 99: 50
Too low. Guess again: 75
Too high. Guess again: 60
Too high. Guess again: 54
Correct. It took you 4 guesses.
"""

import random

def get_choice(attempt):
    """
    return an integer input from the user
    """
    try:
       user_text=''

       if attempt ==1:
           user_text ='Guess a number between 0 and 99:'
        
       choice = int(input(user_text))
    except ValueError:
       return get_choice()
    return choice

def get_random():
    K_HIGH =99
    K_LOW =0
    return random.randint(K_LOW,K_HIGH)

choice =0
rand = get_random()
attempt =0

while (choice != rand):
    attempt += 1
    choice =get_choice(attempt)
    
    if choice > rand:
        print('Too high. Guess again:',end='')
    elif choice < rand:
        print('Too low. Guess again:',end='')
    else:
        print('Correct. It took you {0} guesses.'.format(attempt))


#if __name__ == '__main__':
