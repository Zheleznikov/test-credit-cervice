import requests


def send_rq_to_check_about_credit_info(bench, check_info, body):
    return requests.post(f"{bench}{check_info}", json=body)
