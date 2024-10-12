"""
Author: Bao Nguyen
Assignment / Part: Lab 9 - Q5
Date: April 5
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def organize_into_profits_losses(lst):
    result = []
    current_period = []

    for num in lst:
        if not current_period:
            current_period.append(num)
        else:
            if (num >= 0 and current_period[-1] >= 0) or (num < 0 and current_period[-1] < 0):
                current_period.append(num)
            else:
                result.append(current_period)
                current_period = [num]

    if current_period:
        result.append(current_period)

    return result


def spending_statistics(lst_lsts):
    profit_periods = 0
    loss_periods = 0
    total_balance = sum(sum(period) for period in lst_lsts)

    for period in lst_lsts:
        if period[0] >= 0:
            profit_periods += 1
        else:
            loss_periods += 1

    print("You have had {} periods of subsequent profit.".format(profit_periods))
    print("You have had {} periods of subsequent losses.".format(loss_periods))
    print("Total balance:", total_balance)

    if total_balance <= 0:
        print("You should consider spending less.")
    else:
        print("You're doing great! Keep it up!")


def main():
    weeks_lst = [1, 4, -2, 3, -3, -5, 3]
    organized_weeks_lst = organize_into_profits_losses(weeks_lst)
    print("Here are your spending habits over the last few weeks:", organized_weeks_lst)
    spending_statistics(organized_weeks_lst)


main()
