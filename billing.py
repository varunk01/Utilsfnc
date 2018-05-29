"""
*********************************************************************
* Project : POP1 (Practical Exam)
* Program name : q4.py
* Author : varunk01
* Purpose  : Attempts to solve the question 4 from the exam paper
* Date created : 28/05/2018
*
* Date           Author           Ver     Comment
* 28/05/2018     varunk01         0.1     Initial Version
**********************************************************************

Data:
A9845 Hurley 37.35 R 55
A9846 Hicks 0.00 P 70 139
X0000


Your program should output, for each input record the account number, name,
the type of service, the charge for the month, and the new balance on the account.
Your program must declare, dene and use functions to read each record, to
compute regular charges, to compute premium charges, and to print each output
record.

Rules:

Regular service:
£10.00 for the rst 50 minutes. Charges for over 50
minutes are 20 pence per minute.

Premium service:
£25.00 monthly charge plus

a. for calls made from 6:00am to 6:00pm (daytime), the
rst 75 minutes are free; charges for over 75 minutes are
10 pence per minute

b. for calls made from 6:00pm to 6:00am (o-peak), the
rst 100 minutes are free; charges for over 100 minutes
are 5 pence per minute.
"""


def read_file(i_inp):
    """read file and return words as list
    """
    K_SEPERATOR = ' '
    with open(i_inp) as fp:
        txt = fp.readlines()

    ls = [lines.strip().split(K_SEPERATOR) for lines in txt]
    return ls

def regular_billing(bal,mins):
    K_FREE_MINS =50
    K_SERVICE_CHARGE =10
    K_USAGE_CHARGE = 0.20
    mins = int(mins)
    bal =float(bal)
    amount = (bal -(K_SERVICE_CHARGE + (max(0,mins-K_FREE_MINS)* K_USAGE_CHARGE))) * -1
    bill = bal + amount
    return amount,bill;

def premium_billing(bal,mins,n_mins):
    print('premium_billing',bal,mins,n_mins)
    pass   

def do_billing(item):
    print(item)
    if item[K_SERVICE_LOC]==K_REGULAR:
        bill_line= regular_billing(item[K_BAL_LOC]
                                  ,item[K_MINS_LOC])
        print(bill_line)
    elif item[K_SERVICE_LOC]==K_PREMIUM:
        bill_line = premium_billing(item[K_BAL_LOC]
                                   ,item[K_MINS_LOC]
                                   ,item[K_NIGHT_LOC])
    return bill_line
    

if __name__ == '__main__':
    
    K_REGULAR='R'
    K_PREMIUM ='P'
    K_SERVICE_LOC =3
    K_BAL_LOC=2
    K_MINS_LOC=4
    K_NIGHT_LOC=5
    
    inp = r'D:\pop\working\MockTwo\data\q4inp.txt'
    lineitems = read_file(inp)
    
    for key,item in enumerate(lineitems):
        if item[0] =='X0000':
            break
    
        do_billing(item)


    
