import pytest
from contact import PhoneNumber, WorkPhoneNumber, HomePhoneNumber, OtherPhoneNumber

@pytest.fixture
def phone():
    phone_number = PhoneNumber('469.515.9958')
    work_number = WorkPhoneNumber('469.515.1111')
    home_number = HomePhoneNumber('469.515.2222')
    other_number = OtherPhoneNumber('469.515.3333')