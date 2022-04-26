from asserts.assert_rs import *
from client.check_credit_info_client import send_rq_to_check_about_credit_info
from consts.hosts import check_info
from utils.parse_json import parse_json

body_for_low_rating = parse_json("test_data/data_TC023/TC_0231.json")
body_for_unemployed = parse_json("test_data/data_TC024/TC_0251.json")


def test_tc_0231_low_rating_should_be_denied(bench):
    res = send_rq_to_check_about_credit_info(bench, check_info, body_for_low_rating)
    credit_should_be_denied(res)
    year_payment_should_absent(res)

def test_tc_0241_source_unemployed_should_be_denied(bench):
    res = send_rq_to_check_about_credit_info(bench, check_info, body_for_unemployed)
    credit_should_be_denied(res)
    year_payment_should_absent(res)

