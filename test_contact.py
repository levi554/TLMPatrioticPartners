import pytest
from contact import Person, Contact, WorkPhoneNumber
from contact import Address, HomePhoneNumber, OtherPhoneNumber


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


@pytest.fixture
def contact():
    wp = WorkPhoneNumber('469.515.1111')
    hp = HomePhoneNumber('469.515.2222')
    op = OtherPhoneNumber('469.515.3333')
    address = Address('6512 Briar Lake Trl',
                      'Suite 123', 'Sachse', 'TX', '75048')
    email = None

    c = Contact('Jonathan', 'Livesay', address, (wp, hp, op), email)
    return c


def test_creation_of_person(person1, person2):
    assert person1.first_name == 'Jonathan'
    assert person2.first_name == 'Amber'
    assert person2.last_name == 'Livesay'
    assert person1.last_name == 'Livesay'


def test_creation_of_simple_contact(simple_contact):
    assert simple_contact.first_name == 'Jonathan'
    assert simple_contact.phone_numbers is not None
    assert simple_contact.phone_numbers == []
