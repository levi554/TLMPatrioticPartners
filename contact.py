import uuid


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Contact(Person):

    def __init__(self, first_name, last_name, addresses=None, phone_numbers=None, email_addresses=None):
        super().__init__(first_name, last_name)
        if addresses is None:
            self.addresses = []
        else:
            self.addresses = addresses

        if phone_numbers is None: 
            self.phone_numbers = []
        else:
            self.phone_numbers = phone_numbers

        if email_addresses is None:
            self.email_addresses = []
        else:
            self.email_addresses = email_addresses

    def add_email_address(self, email_address):
        if email_address not in self.email_addresses:
            self.email_addresses.append(email_address)

    def delete_email_address(self, email_address):
        if email_address not in self.email_addresses:
            self.email_addresses.remove(email_address)

    def add_phone_number(self, phone_number):
        if phone_number not in self.phone_numbers:
            self.phone_numbers.append(phone_number)

    def delete_phone_number(self, phone_number):
        if phone_number not in self.phone_numbers:
            self.phone_numbers.append(phone_number)


class Type:
    pass


class Address():

    def __init__(self, street1, street2, city, state, zip_code):
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip_code = zip_code


class PhoneNumber():

    def __init__(self, phone_number, phone_type=None, phone_number_id=None):
        if phone_number_id is None:
            self.phone_number_id = uuid.uuid4()
        else:
            self.phone_number_id = phone_number_id
        if phone_type is None:
            self.phone_type = 'phone_type'
        else:
            self.phone_type = phone_type
        self.phone_number = phone_number


class WorkPhoneNumber(PhoneNumber):

    def __init__(self, phone_number, phone_type=None, phone_number_id=None):
        super().__init__(phone_number, phone_type, phone_number_id)
        self.phone_type = 'work_phone'


class HomePhoneNumber(PhoneNumber):

    def __init__(self, phone_number, phone_type=None, phone_number_id=None):
        super().__init__(phone_number, phone_type, phone_number_id)
        self.phone_type = 'home_phone'


class OtherPhoneNumber(PhoneNumber):

    def __init__(self, phone_number, phone_type=None, phone_number_id=None):
        super().__init__(phone_number, phone_type, phone_number_id)
        self.phone_type = 'other_phone'


class Email:

    def __init__(self, email_address, email_address_id=None):
        if email_address_id is None:
            self.email_address_id = uuid.uuid4
        else:
            self.email_address_id = email_address_id        
        self.email_address = email_address
        self.email_address_type = 'email'

