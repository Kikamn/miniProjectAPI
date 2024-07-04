import pytest
import requests
from assertpy import assert_that

from setting.endpoint import api_user
from faker import Faker

faker = Faker()
#  pytest test/test_POST_USER/test_post_negatif.py -- cara jalain 1 class saja
@pytest.mark.QaseIO(13)
def test():
    randomEmail = faker.email()
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 76faab1ff917d8d72e6a538fc435ab8a5a718198b4dc431ee8e8d3726702876e"
    }

    payload = {
        "name": "",
        "gender": "female",
        "email": randomEmail,
        "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)
    #print(req.json())

    #VALIDATOR
    status_code = req.status_code
    resfield = req.json()[0]["field"]
    resMessage = req.json()[0]["message"]

    #ASSERT THAT (buat cek validasi)
    assert_that(status_code).is_equal_to(422)
    assert_that(resfield).is_equal_to("name")
    assert_that(resMessage).is_equal_to("can't be blank")
