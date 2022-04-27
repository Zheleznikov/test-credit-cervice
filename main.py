import math

from utils.calc import calc_year_payment


def print_hi():
    print(-math.log10(0.1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data =     {
    "age": 30,
    "sex": "female",
    "incomingSource": "employee",
    "incomeForLastYear": 2.1,
    "creditRating": -1,
    "requestedAmount": 1,
    "loanRepaymentTime": 20,
    "goal": "personal loan"
  }

    print(calc_year_payment(data))
