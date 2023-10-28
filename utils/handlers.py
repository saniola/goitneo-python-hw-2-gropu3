from adressbook import AddressBook
from decorators.input_error import input_error
from utils.is_valid_phone import is_valid_phone
from record import Record

@input_error
def add_contact(args, contacts: AddressBook):
    name, phone = args
    name = name.lower()

    if not is_valid_phone(phone):
        raise TypeError

    if name in contacts:
        record = contacts[name]
        record.add_phone(phone)
    else:
        record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)

    return f"Contact {name} with phone number {phone} added."

@input_error
def change_contact(args, contacts: AddressBook):
    name, old_phone, new_phone = args
    name = name.lower()

    if not is_valid_phone(new_phone):
        raise TypeError

    if name in contacts:
        record = contacts[name]

        try:
            record.edit_phone(old_phone, new_phone)
            return f"Contact {name} updated. New phone number: {new_phone}."
        except ValueError as e:
            raise ValueError(str(e))
    else:
        raise KeyError

@input_error
def show_phone(args, contacts: AddressBook):
    name = args[0]
    name = name.lower()

    if name in contacts:
        record = contacts[name]
        phone_numbers = [phone.value for phone in record.phones]
        return f"Phone numbers for {name}: {', '.join(phone_numbers)}."
    else:
        raise KeyError

@input_error
def show_all(args, contacts: AddressBook):
    if len(args) > 0:
        raise ValueError

    if not contacts:
        raise KeyError

    if len(contacts) > 0:
        result = "All saved contacts with phone numbers:\n"

        for name, record in contacts.items():
            phone_numbers = [phone.value for phone in record.phones]
            result += f"{name}: {', '.join(phone_numbers)}\n"
        return result
