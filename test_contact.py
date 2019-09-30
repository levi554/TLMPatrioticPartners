import uuid


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class contact(Person):

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


class PhoneNumber():

    def __init__(self, phone_number, type=None, uuid=None:
        if uuid is None:
            self.uuid = uuid.uuid4()
        else:
            self.uuid = uuid
        self.type = None
        self.phone_number = phone_number


