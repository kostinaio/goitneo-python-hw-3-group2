
from address_book import AddressBook, Phone, PhoneError, Record, BirthdayError
from datetime import datetime
from birthday_on_week import get_birthdays_per_week


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please enter the correct format. Command is invalid."
        except BirthdayError as e:
            return str(e)
    return inner


@input_error
def add_contact(args, book):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    try:
        record = book.find(name)
        try:
            record.add_phone(phone)
            return "Phone added to existing contact."
        except PhoneError as e:
            return str(e)
    except KeyError:
        try:
            record = Record(name)
            record.add_phone(phone)
            book.add_record(record)
            return "Contact added."
        except PhoneError as e:
            return str(e)

@input_error
def change_contact(args, book):
    if len(args) != 2:
        raise ValueError
    name, new_phone = args
    try:
        record = book.find(name)
        Phone(new_phone)
        record.edit_phone(record.phones[0].value, new_phone)
        return "Contact updated."
    except (KeyError, PhoneError) as e:
        return str(e)

@input_error    
def show_phone(args, book):
    if len(args) < 1:
        return "Invalid command. Please enter: phone [name]"     
    name = args[0]
    try:
        record = book.find(name)
        phones = ', '.join(str(phone) for phone in record.phones)
        return f"Phone number for {name}: {phones}"
    except KeyError:
        raise KeyError
    
def show_all(book):
    if not book.data:
        return "Address book is empty."
    all_contacts_info = []
    for name, record in book.data.items():
        contact_info = f"Contact name: {name}, phones: {'; '.join(p.value for p in record.phones)}"
        all_contacts_info.append(contact_info)
    return "\n".join(all_contacts_info)

@input_error
def add_birthday(args, book):
    if len(args) != 2:
        return "Give me name and birthday please."
    name, birthday = args
    try:
        record = book.find(name)
        record.add_birthday(birthday)
        return "Birthday added."
    except KeyError:
        raise KeyError

@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    try:
        record = book.find(name)
        birthday = record.birthday.value if record.birthday else 'Not set'
        return f"Birthday for {name}: {birthday}"
    except KeyError:
        raise KeyError

    
def birthdays(book):
    users = {name: record.birthday.value for name, record in book.data.items()}
    birthdays_info = get_birthdays_per_week(users)
    return birthdays_info



def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()