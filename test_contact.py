from contact import Person, Contact, WorkPhoneNumber, HomePhoneNumber, OtherPhoneNumber


def test_creation_of_person():
    person1 = Person('Jonathan', 'Livesay')
    person2 = Person('Amber', '')

    assert person1.first_name == 'Jonathan'
    assert person2.first_name == 'Amber'
    assert person2.last_name == ''
    assert person1.last_name == 'Livesay'


def test_creation_of_simple_contact():
    contact1 = Contact('Jonathan', 'Livesay')

    assert contact1.first_name == 'Jonathan'
    assert contact1.phone_numbers is not None
    assert contact1.phone_numbers == []
