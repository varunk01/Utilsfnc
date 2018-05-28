"""
Write a program that asks the user how many Fibonacci numbers to generate and
then generates them. Make sure to ask the user to enter the number of numbers
in the sequence to generate. (Hint: The Fibonacci sequence is a sequence of
numbers where the next number in the sequence is the sum of the previous two
numbers in the sequence.
"""

def user_input():
    try:
        n = int(input('enter number of fibo numbers required: '))
    except ValueError:
        print('invalid input')
        return -1
    return n


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
      
if __name__  == '__main__':
    a = user_input()
    print(list(fib(a)))
