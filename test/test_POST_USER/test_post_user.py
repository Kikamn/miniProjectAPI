import pytest
import requests
from assertpy import assert_that

from setting.endpoint import api_user
from faker import Faker

faker = Faker()
@pytest.mark.QaseIO(15)
def test():
    randomName = faker.name()
    randomEmail = faker.email()
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 76faab1ff917d8d72e6a538fc435ab8a5a718198b4dc431ee8e8d3726702876e"
    }

    payload = {
        "name": randomName,
        "gender": "female",
        "email": randomEmail,
        "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)
    #print(req.json())

    #VALIDATOR
    status_code = req.status_code
    resName = req.json().get("name")
    resEmail = req.json().get("email")

    #ASSERT THAT
    assert_that(status_code).is_equal_to(201)
    assert_that(resName).is_equal_to(randomName)
    assert_that(resEmail).is_equal_to(randomEmail)
