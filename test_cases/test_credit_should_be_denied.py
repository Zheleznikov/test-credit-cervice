import pytest

from asserts.assert_rs import *
from client.check_credit_info_client import send_rq_to_check_about_credit_info
from consts.hosts import check_info
from utils.calc import calc_year_payment
from utils.parse_json import parse_json

credit_rq_list = parse_json("test_data/TC052/TC0522.json")


@pytest.mark.parametrize("body", credit_rq_list)
def test_tc_0522_credit_should_be_denied(bench, body):
    res = send_rq_to_check_about_credit_info(bench, check_info, body)
    credit_should_be_denied(res)
    year_payment_should_absent(res)
    # todo добавить больше тел запроса с разными параметрами для проверки

