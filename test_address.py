import pytest
from contact import Address

@pytest.fixture
def address():
    address = Address('6512 Briar Lake Trl', 'Room 123', 'Sachse', 'TX', '75048')
    return address


def test_address_creation(address):
    assert 'Sachse' == address.city