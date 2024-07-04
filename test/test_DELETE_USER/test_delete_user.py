import pytest
import requests
from assertpy import assert_that

from setting.endpoint import api_user
from faker import Faker

faker = Faker()
#  pytest test/test_POST_USER/test_post_negatif.py -- cara jalain 1 class saja
@pytest.mark.QaseIO(16)
def test():
    # 1. CREATE NEW USER
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
    idNewUser = req.json().get("id") # untuk dapetin id saat create

    #2. UPDATE USER

    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 76faab1ff917d8d72e6a538fc435ab8a5a718198b4dc431ee8e8d3726702876e"
    }

    req = requests.delete(f"{api_user}/{idNewUser}", headers=head) # nnti akan jadi https://gorest.co.in/public/v2/users/6998653
    # print(req.json())

    #VALIDATOR
    status_code = req.status_code

    #ASSERT THAT
    assert_that(status_code).is_equal_to(204)
