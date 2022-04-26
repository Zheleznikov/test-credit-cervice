import pytest

from asserts.assert_rs import *
from client.check_credit_info_client import send_rq_to_check_about_credit_info
from consts.hosts import check_info
from utils.parse_json import parse_json

list_for_check_amount_and_source_testing_pos = parse_json("test_data/data_TC022/TC_0221.json")
list_for_check_amount_and_source_testing_neg = parse_json("test_data/data_TC022/TC_0222.json")


@pytest.mark.parametrize("body", list_for_check_amount_and_source_testing_pos)
def test_tc_0221_required_amount_and_incoming_source_should_be_approved(bench, body):
    res = send_rq_to_check_about_credit_info(bench, check_info, body)
    credit_should_be_approved(res)
    year_payment_should_exist(res)


def test_tc_0222_required_amount_and_incoming_source_should_be_denied(bench):
    res = send_rq_to_check_about_credit_info(bench, check_info, list_for_check_amount_and_source_testing_neg)
    credit_should_be_denied(res)
    year_payment_should_absent(res)
