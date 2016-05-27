#! /usr/bin/env python

"""
Small set of tools for calculating HDB loan repayments. Seems to tally.
"""

def find_months(balance, monthly, months, rate):
    """
    How many months before loan balance drops below zero.
    We assume interest only compounds once a year.
    """
    balance -= (12 * monthly)
    if balance > 0:
        return find_months(balance * (1 + rate), monthly, months + 12, rate)
    else:
        return months

if __name__ == "__main__":
    my_rate = float(raw_input("What percent interest are you paying? ")) / 100
    my_balance = float(raw_input("What is your loan amount? "))
    my_repay = float(raw_input("Paying per month? "))
    my_months = find_months(my_balance, my_repay, 0, my_rate)
    print "You're free in {} months ({} years).".format(my_months, my_months / 12)
