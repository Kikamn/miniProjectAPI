import pytest
import requests
from assertpy import assert_that

from setting.endpoint import api_user
from faker import Faker

faker = Faker()
#  pytest test/test_POST_USER/test_post_negatif.py -- cara jalain 1 class saja
@pytest.mark.QaseIO(11)
def test():
    randomName = faker.name()

    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 76faab1ff917d8d72e6a538fc435ab8a5a718198b4dc431ee8e8d3726702876e"
    }

    payload = {
        "name": randomName,
        "gender": "female",
        "email": "kikamn@gmail.com",
        "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)
    #print(req.json())

    #VALIDATOR
    status_code = req.status_code
    # AMBIL PRETTY DARI API
    resfield = req.json()[0]["field"]
    resMessage = req.json()[0]["message"]

    #ASSERT THAT (buat cek validasi)
    assert_that(status_code).is_equal_to(422)
    # SAAT EMAIL BLANK
    #assert_that(resfield).is_equal_to("email")
    #assert_that(resMessage).is_equal_to("can't be blank")

    #EMAIL SUDAH TERDAFTAR/ DUPLICATE EMAIL
    assert_that(resfield).is_equal_to("email")
    assert_that(resMessage).is_equal_to("has already been taken")