# Contact Book
A basic Python project for managing contacts. The Contact Book allows you to add, update, remove, and display contact information.

## Project Implementation
TThe project consists of the following files and directories.

```
.
├── README.md
├── contact_book.py
└── main.py
```

The project structure was designed to be simple and clean.

- `README.md`: this document providing project description and documentation
- `contact_book.py`: the Python script that defines the ContactBook class which encapsulates the core functionalities of the application
- `contacts.py`: the main script which interacts with the user and uses ContactBook class methods to provide the desired functionality


### ContactBook Class
The core logic of the application is implemented in `ContactBook` class:

- The `add_contact` method allows for new entries to be made to the 'book'. Each entry must be unique by name.
- The `update_contact` method permits updates to contact information.

- The `show_contacts` method lists all contacts in the address book along with their information.
- The `remove_contact` method allows for existing contacts to be removed from the book.


The `contacts.py` file serves as an interface between the user and the `ContactBook` class instance. It gets user inputs, calls the necessary methods and handles the application flow.

## User Interface
The user interface can be implemented using a command-line interface (CLI), a graphical user interface (GUI), or any other preferred method.

## Installation and Usage
Clone the repository:
git clone https://github.com/your-username/contact-book.git

Navigate to the project directory:
cd contact-book

```bash
python main.py
```