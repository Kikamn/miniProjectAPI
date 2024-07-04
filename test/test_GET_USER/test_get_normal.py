import pytest
import requests
from assertpy import assert_that

from setting.endpoint import api_user

@pytest.mark.QaseIO(18)
def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 76faab1ff917d8d72e6a538fc435ab8a5a718198b4dc431ee8e8d3726702876e"
    }
    req = requests.get(api_user, headers=head)
    #print(req.json())

    #respName = req.json().get("name")
    #VALIDATOR
    status_code = req.status_code
    respID = req.json()[0]["id"] #ambil dari indeks ke brp utk idnya
    respName = req.json()[0]["name"]
    respEmail = req.json()[0]["email"]
    respGender = req.json()[0]["gender"]
    respStatus = req.json()[0]["status"]

    #ASSERT THAT
    assert_that(status_code).is_equal_to(200)
    assert_that(respID).is_not_none()
    assert_that(respName).is_not_none()
    assert_that(respEmail).is_not_none()
    assert_that(respGender).is_not_none()
    assert_that(respStatus).is_not_none()

    assert_that(respID).is_type_of(int)
    assert_that(respEmail).contains("@")
    assert_that(respGender).is_in("female", "male")
    assert_that(respStatus).is_in("active", "inactive")