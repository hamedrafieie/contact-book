from collections import defaultdict

class ContactBook():
    
    def __init__(self):
        self.contacts = defaultdict(dict)

    def add_contact(self, name: str, number: str, email: str = None):
        
        if name in self.contacts:
            print('Contact already exists!!')
            return

        self.contacts[name]['number'] = number
        self.contacts[name]['email'] = email


    def remove_contact(self, name: str):

        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} removed')
        else:
            print(f'{name} does not exist in the contact book')
    

    def update_contact(self, name: str, number: str = None, email: str = None):
        if name in self.contacts:
            
            if number:
                self.contacts[name]['number'] = number
            if email:
                self.contacts[name]['email'] = email

        else: 
            print(f'{name} does not exist in the contact book')   


    def show_contacts(self):
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['number']}")
            print(f"Email: {info['email']}")
            print('-' * 50)


if __name__ == '__main__':
    book = ContactBook()

    while True:
        print('\n\nWelcome to contact book application!')
        print('1. Add Contact')
        print('2. Edit Contact')
        print('3. View Contacts')
        print('4. Delete Contact')
        print('5. Quit')

        user_choice = input('Please choose an option: ')

        if user_choice == '5':
            break

        elif user_choice == '1':
            name = input('\nEnter contact name: ')
            number = input('Enter contact number: ')
            email = input('Enter contact email: ')

            book.add_contact(name, number, email)

        elif user_choice == '2':
            name = input('\nEnter contact name: ')
            number = input('Enter contact number: ')
            email = input('Enter contact email: ')

            book.update_contact(name, number, email)

        elif user_choice == '3':
            print('\n\nList of contacts:')
            book.show_contacts()

        elif user_choice == '4':
            name = input('\nEnter contact name: ')
            book.remove_contact(name)           