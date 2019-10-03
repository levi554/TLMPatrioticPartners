import pytest
from contact import Person, Contact, WorkPhoneNumber, HomePhoneNumber, OtherPhoneNumber


@pytest.fixture
def person1():
    p1 = Person('Jonathan', 'Livesay')
    return p1

@pytest.fixture
def person2():
    p2 = Person('Amber', 'Livesay')
    return p2

@pytest.fixture
def simple_contact():
    sc = Contact('Jonathan', 'Livesay', None, None, None)
    return sc


def test_creation_of_person(person1, person2):
    assert person1.first_name == 'Jonathan'
    assert person2.first_name == 'Amber'
    assert person2.last_name == 'Livesay'
    assert person1.last_name == 'Livesay'


def test_creation_of_simple_contact(simple_contact):
    assert simple_contact.first_name == 'Jonathan'
    assert simple_contact.phone_numbers is not None
    assert simple_contact.phone_numbers == []


def test_work_phone_number_in_contact():
    work_phone_number = WorkPhoneNumber('469.515.9958')
    contact1 = Contact('Jonathan', 'Livesay', addresses=None, phone_numbers=work_phone_number, email_addresses=None)

    assert contact1.first_name == 'Jonathan'

