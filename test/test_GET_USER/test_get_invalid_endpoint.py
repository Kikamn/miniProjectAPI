import pytest
import requests
from assertpy import assert_that

from setting.endpoint import api_user_wrong

@pytest.mark.QaseIO(17)
def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 76faab1ff917d8d72e6a538fc435ab8a5a718198b4dc431ee8e8d3726702876e"
    }
    req = requests.get(api_user_wrong, headers=head)
    #print(req.json())

    #respName = req.json().get("name")
    #VALIDATOR
    status_code = req.status_code

    #ASSERT THAT
    assert_that(status_code).is_equal_to(404)
