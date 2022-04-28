from asserts.assert_rs import *
from client.check_credit_info_client import send_rq_to_check_about_credit_info
from consts.hosts import check_info
from utils.parse_json import parse_json

body1 = parse_json("test_data/data_TC031/TC_0311.json")
body2 = parse_json("test_data/data_TC031/TC_0312.json")

# todo параметризизовать тесты, используя дополнительные тестовые данные
def test_tc_0311_should_be_calc_as_min(bench):
    res1 = send_rq_to_check_about_credit_info(bench, check_info, body1[0])
    credit_should_be_denied(res1)
    year_payment_should_absent(res1)

    res2 = send_rq_to_check_about_credit_info(bench, check_info, body1[1])
    credit_should_be_approved(res2)
    year_payment_should_exist(res2)


def test_tc_0312_should_be_calc_as_min(bench):
    res1 = send_rq_to_check_about_credit_info(bench, check_info, body2[0])
    credit_should_be_denied(res1)
    year_payment_should_absent(res1)

    res2 = send_rq_to_check_about_credit_info(bench, check_info, body2[1])
    credit_should_be_approved(res2)
    year_payment_should_exist(res2)



