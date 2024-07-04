import requests

from setting.endpoint import TOKEN_QASE_IO, PROJECT_QASE_IO, TEST_RUNING_QASE_IO, api_result


def update_test_result(test_caseID, status):
    head = {
        "accept": "application/json",
        "content-type": "application/json",
        "Token": TOKEN_QASE_IO
    }

    payload = {
        "case_id": test_caseID,
        "status": status
    }

    requests.post(f"{api_result}/{PROJECT_QASE_IO}/{TEST_RUNING_QASE_IO}", headers=head, json=payload)