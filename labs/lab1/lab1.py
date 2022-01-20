"""
Cade Atkins
lab1.py

Q: Find the monthly interest on an account

I certify that this assignment is entirely my own work.
"""

def monthly_interest():
    ### avgerage daily balance
    net_balance = eval(input("Net balance for the month: "))
    cycle_days = eval(input("Billing cycle length: "))
    step1 = net_balance * cycle_days
    payment = eval(input("Previous payment amount: "))
    day_paid = eval(input("How many days did it take to pay: "))
    step2 = (cycle_days - day_paid) * payment
    step3 = step1 - step2
    step4 = step3 / cycle_days
    ###
    annual_interest = eval(input("What is your annual interest: "))
    m_interest = annual_interest / 12

    final = m_interest * step4

    print(final)
monthly_interest()
###



