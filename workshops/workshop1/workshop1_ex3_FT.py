import numpy as np


def tax(income):
    """
    Return the taxes owed for a given income.

    Parameters
    ------
    income
        gross income

    Returns
    ------
    tax owed
    """
    

    if income > 700000:
        taxes = (0.2*(700000-300000)+0.35*(income-700000))
    elif income > 300000:
        taxes = 0.2 * (income-300_000)
    else:
        taxes = 0

    return taxes

incomes = np.linspace(0, 1_200_000, 13)

taxes_loop = []

for income in incomes:
    #compute taxes for current income level
    taxes = tax(income)
    #append to list
    taxes_loop.append(taxes)
    #income after tax
    net_income = income-taxes

    print(f'Gross income: {income:10.0f};',
          f'Taxes: {taxes:10.0f}',
          f'Net income {net_income:10.0f}')





print(taxes_loop)
print(tax(700_001))