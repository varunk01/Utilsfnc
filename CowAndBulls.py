"""
Create a program that will play the \cows and bulls" game with the user. The
game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a
\cow". For every digit the user guessed correctly in the wrong place is a \bull".
Every time the user makes a guess, tell them how many \cows" and \bulls" they
have. Once the user guesses the correct number, the game is over. Keep track of
the number of guesses the user makes throughout the game and tell the user at
the end.
"""


import random
def do_guess():
    K_LOW,K_HIGH = 1000,9999
    guess = random.randint(K_LOW,K_HIGH)
    return guess

def get_choice():
    try:
       choice = int(input('enter a 4 digit number: '))
    except ValueError:
       return get_choice()
    return choice

def match(rand_guess,choice):
    cow =0
    bull=0
    s1 = list(str(rand_guess))
    s2 = list(str(choice))
    s2 = [i for i in s2 if i in s1]
    return len(s2), len(s1)-len(s2)

if __name__  == '__main__':
    cow =0
    bull=0
    turns=0
    rand_guess = do_guess()
    while(cow<4):
        
        choice = get_choice()
        cow,bull = match(rand_guess,choice)
               
        print('cows:{0} bulls:{1}'.format(cow,bull))
        turns+=1

    print('right choice in {0} turns'.format(turns))
