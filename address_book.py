
from collections import UserDict
from datetime import datetime
from birthday_on_week import get_birthdays_per_week

class PhoneError(Exception):
    pass

class BirthdayError(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise PhoneError("Phone number must be 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except BirthdayError:
            raise BirthdayError("Birthday must be in DD.MM.YYYY format.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone
                return new_phone
        raise ValueError("Phone number not found.")
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return f"Birthday added: {birthday}"

    def find_phone(self, phone):
        for p in self.phones:
         if str(p) == phone:
            return p
        raise ValueError("Phone number not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name not in self.data:
            raise KeyError("Contact not found.")
        return self.data[name]

    def delete(self, name):
        if name not in self.data:
            raise KeyError("Contact not found.")
        del self.data[name]

    def birthdays(self):
        users = {name: {"birthday": record.birthday.value} for name, record in self.data.items()}
        return get_birthdays_per_week(users)



# Блок тестування

# Створення нової адресної книги
# book = AddressBook()

# Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
# book.add_record(john_record)

# Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# Виведення: Contact name: John, phones: 1112223333; 5555555555
# print(john)

# Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}") 

# Видалення запису Jane
# book.delete("Jane")

# Виведення всіх записів у книзі
# for name, record in book.data.items():
#    print(record)
