import pytest
from contact import PhoneNumber, WorkPhoneNumber, HomePhoneNumber, OtherPhoneNumber

@pytest.fixture
def phone():
    phone = PhoneNumber('469.515.1111')
    return phone

@pytest.fixture
def work_phone():
    work_phone = WorkPhoneNumber('469.515.2222')
    return work_phone

@pytest.fixture
def home_phone():
    home_phone = HomePhoneNumber('469.515.3333')
    return home_phone

@pytest.fixture
def other_phone():
    other_phone = OtherPhoneNumber('469.515.4444')
    return other_phone


def test_phone_number(phone):
    assert phone.phone_number == '469.515.1111'


def test_phone_number_id_not_blank(phone):
    print(f'Phone Number UUID: {phone.phone_number_id}')
    assert phone.phone_number_id is not None
    assert phone.phone_number_id != ''
