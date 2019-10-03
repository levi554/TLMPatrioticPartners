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


def test_phone_number_id_does_not_match_id_from_another_phone_number(phone):
    phone2 = PhoneNumber('469.853.1111')
    assert phone.phone_number_id is not phone2.phone_number_id


def test_to_see_that_new_uuid_is_generated_if_phone_number_is_reset(phone):
    phone_id = phone.phone_number_id
    phone = None
    phone = PhoneNumber('469.515.1111')
    assert phone_id is phone.phone_number_id
