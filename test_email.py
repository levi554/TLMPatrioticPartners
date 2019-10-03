import pytest
from contact import Email


@pytest.fixture
def email():
    email = Email('jonl316@pm.me')
    return email


def test_email_creation(email):
    assert email.email_address == 'jonl316@pm.me'