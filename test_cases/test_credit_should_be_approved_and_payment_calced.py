import pytest

from asserts.assert_rs import *
from client.check_credit_info_client import send_rq_to_check_about_credit_info
from consts.hosts import check_info
from utils.calc import calc_year_payment
from utils.parse_json import parse_json

credit_rq_list = parse_json("test_data/TC052/TC0521.json")


@pytest.mark.parametrize("body", credit_rq_list)
def test_tc_0521_credit_should_be_approved_payment_caled_correctly(bench, body):
    res = send_rq_to_check_about_credit_info(bench, check_info, body)
    credit_should_be_approved(res)
    expected_year_payment = calc_year_payment(body)
    year_payment_should_be_correct(res, expected_year_payment)
    # todo подготовить дополнительные тестовые данные
