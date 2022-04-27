import math


def calc_year_payment(data):
    amount = data.get("requestedAmount")
    time = data.get("loanRepaymentTime")
    mod = calc_mod(data)
    changed_rate = 10 + mod
    k = 1 + time * (changed_rate / 100)
    payment = (amount / time) * k
    return to_fixed(payment)


def calc_mod(data):
    source = data.get("incomingSource")
    rating = data.get("creditRating")
    amount = data.get("requestedAmount")
    goal = data.get("goal")

    mod = 0
    if goal == 'mortgage':
        mod -= 2
    if goal == 'business development':
        mod -= 0.5
    if goal == 'personal loan':
        mod += 1.5

    if source == 'passive income':
        mod += 0.5
    if source == 'employee':
        mod -= 0.25
    if source == 'own business':
        mod += 0.25

    if rating == -1:
        mod += 1.5
    if rating == 1:
        mod -= 0.25
    if rating == 2:
        mod -= 0.75

    add_mod = -math.log10(amount)
    mod += add_mod
    return mod


def to_fixed(numObj, digits=3):
    return f"{numObj:.{digits}f}"
