import pytest

from asserts.assert_rs import *
from client.check_credit_info_client import send_rq_to_check_about_credit_info
from consts.hosts import check_info
from utils.parse_json import parse_json

list_for_age_male_testing_pos = parse_json("test_data/data_TC021/TC_0211.json")
list_for_age_male_testing_neg = parse_json("test_data/data_TC021/TC_0212.json")
list_for_age_female_testing_pos = parse_json("test_data/data_TC021/TC_0213.json")
list_for_age_female_testing_neg = parse_json("test_data/data_TC021/TC_0214.json")


@pytest.mark.parametrize("body", list_for_age_male_testing_pos)
def test_tc_0211_retirement_age(bench, body):
    res = send_rq_to_check_about_credit_info(bench, check_info, body)
    credit_should_be_approved(res)
    year_payment_should_exist(res)


@pytest.mark.parametrize("body", list_for_age_male_testing_neg)
def test_tc_0212_retirement_age(bench, body):
    res = send_rq_to_check_about_credit_info(bench, check_info, body)
    credit_should_be_denied(res)
    year_payment_should_absent(res)


@pytest.mark.parametrize("body", list_for_age_female_testing_pos)
def test_tc_0213_retirement_age(bench, body):
    res = send_rq_to_check_about_credit_info(bench, check_info, body)
    credit_should_be_approved(res)
    year_payment_should_exist(res)


@pytest.mark.parametrize("body", list_for_age_female_testing_neg)
def test_tc_0214_retirement_age(bench, body):
    res = send_rq_to_check_about_credit_info(bench, check_info, body)
    credit_should_be_denied(res)
    year_payment_should_absent(res)
