import pytest
from contact import Address

@pytest.fixture
def address():
    address = Address('6512 Briar Lake Trl', 'Room 123', 'Sachse', 'TX', '75048')
    return address


def test_address_creation(address):
    assert 'Sachse' == address.city


def test_address_street1(address):
    assert address.street1 == '6512 Briar Lake Trl'


def test_address_street2(address):
    assert address.street2 == 'Room 123'


def test_address_state(address):
    assert address.state == 'TX'


def test_address_zip_code(address):
    assert address.zip_code == '75048'
    assert type(address.zip_code) != int


def test_address_is_not_None_type(address):
    assert address is not None


def test_address_is_not_blank(address):
    assert address.street1 is not ''
    assert address.street2 is not ''
    assert address.city is not ''
    assert address.state is not ''
    assert address.zip_code is not ''

