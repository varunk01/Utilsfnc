"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
"""


def user_input():
    try:
        n = int(input('enter number: '))
    except ValueError:
        print('invalid input')
        return -1
    return n

def check_prime(i_n):
    n = i_n
    prime = True        
    for i in range(2, round(n/2)+1):
        if n%i == 0:
            prime = False
            break
    return (prime)


if __name__  == '__main__': 
   n =  user_input()
   if n>0:
     print(check_prime(n))
