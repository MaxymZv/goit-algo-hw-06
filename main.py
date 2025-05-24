from collections import UserDict

#Making class Field that will be used as a base class for Name and Phone
class Field:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass

#Making class Phone 
class Phone(Field):
    def __init__(self, value):
        value = str(value)
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be a 10-digit number.")
        super().__init__(value)

# Making class Record that will hold contact information
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f'Contact name: {self.name.value}, Phones: {",".join(str(p) for p in self.phones)}'
    
#Method for adding phone number    
    def add_phone(self, phone):
        if isinstance(phone, str):
            phone = Phone(phone)
        self.phones.append(phone)

#Method for removing phone number
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

#Method for editing phone number
    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                if isinstance(new_phone, str):
                    new_phone = Phone(new_phone)
                self.phones[index] = Phone(new_phone)
                return
        raise ValueError(f"Phone number {old_phone} not found in record.") 

#Method for finding phone number 
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        else:
            return None

#Making class Adressbook that inherits from UserDict    
class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record
    
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def find(self, name):
        return self.data.get(name, None)
    
    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
    



#Some testing        
book = AddressBook()

john_record = Record('John')
john_record.add_phone('1234567890')
john_record.add_phone('0987612321')
book.add_record(john_record)

jane_record = Record('Jane')
jane_record.add_phone("9876543210")
book.add_record(jane_record)


john = book.find('John')

john.edit_phone('1234567890', '1112223333')

print(john)

found_phone = john.find_phone('1112223333')

print(f'{john.name}: {found_phone}')

book.delete('Jane')

print(book)

