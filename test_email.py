import pytest
from contact import Email, WorkEmail, HomeEmail, OtherEmail


@pytest.fixture
def email():
    email = Email('jonl316@pm.me')
    return email


@pytest.fixture
def work_email():
    wem = WorkEmail('jonathan.livesay@jnteam.org')
    return wem

@pytest.fixture
def home_email():
    hem = HomeEmail('jonl316@gmail.com')
    return hem

@pytest.fixture
def other_email():
    oem = OtherEmail('jonathan.livesay@gmail.com')
    return oem


def test_email_creation(email):
    assert email.email_address == 'jonl316@pm.me'


def test_work_email_creation(work_email):
    assert work_email.email_address == 'jonathan.livesay@jnteam.org'


def test_home_email_creation(home_email):
    assert home_email.email_address == 'jonl316@gmail.com'


def test_other_email_creation(other_email):
    assert other_email.email_address == 'jonathan.livesay@gmail.com'
