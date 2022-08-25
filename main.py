from collections import UserDict


class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name: Name = name
        self.phone: list[Phone] = [phone] if phone else []

    def __repr__(self) -> str:
        return f"{self.name.value} : {' '.join(phone.value for phone in self.phone)}"

    def add_phone(self, *phone: Phone) -> None:
        self.phone.extend(phone)

    def change_phone(self, old_phone: Phone, new_phone: Phone) -> None:
        for phone in self.phone:
            if phone.value == old_phone.value:
                phone.value = new_phone.value
                return
        print(f"Phone number '{old_phone.value}' does not exist!")

    def remuve_phone(self, phone_remuve: Phone) -> None:
        for phone in self.phone:
            if phone.value == phone_remuve.value:
                self.phone.remove(phone)
                return
        print(f"Phone number '{phone_remuve.value}' does not exist!")


class AddressBook(UserDict):
    data: dict[str, Record] = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record
