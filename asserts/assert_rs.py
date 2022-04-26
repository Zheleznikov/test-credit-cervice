def credit_should_be_approved(res):
    assert res.json().get("isCreditApproved") == True


def credit_should_be_denied(res):
    assert res.json().get("isCreditApproved") == False


def year_payment_should_exist(res):
    assert res.json().get("yearPayment") is not None


def year_payment_should_absent(res):
    assert res.json().get("yearPayment") is None


def year_payment_should_be_correct(res, year_payment):
    assert res.json().get("yearPayment") == year_payment
