from adressbook import AddressBook
from decorators.input_error import input_error
from utils.is_valid_phone import is_valid_phone
from record import Record

@input_error
def add_contact(args, contacts: AddressBook):
    name, phone = args
    name = name.lower()
    user: Record = Record(name)
    user.add_phone(phone)
    contacts.add_record(user)

    return f"Contact {name} with phone number {phone} added."

@input_error
def change_contact(args, contacts: AddressBook):
    name, old_phone, new_phone = args
    name = name.lower()
    user: Record = contacts.find(name)
    phone = user.find_phone(old_phone)
    user.edit_phone(phone, new_phone)

def show_phone(args, contacts: AddressBook):
    name = args[0]
    name = name.lower()
    user: Record = contacts.find(name)

    return f"Phone numbers for {name}: {', '.join(user.phones)}."

def show_all(args, contacts: AddressBook):
    if len(args) > 0:
        raise ValueError

    if not contacts:
        raise KeyError

    if len(contacts.data.items()) > 0:
        print("All saved contacts with phone numbers:")

        for name, record in contacts.data.items():
           print(record)
