# 0x00. AirBnB Clone - The Console

Welcome to the AirBnB Clone - The Console project! This command-line interface (CLI) application is designed to simulate the basic functionality of the AirBnB platform, allowing you to interact with objects and data related to property rentals.

## Description of the Command Interpreter

The command interpreter is a text-based interface that allows you to interact with the AirBnB clone application. It provides various commands to manage users, places, reviews, and more.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine using:
git clone https://github.com/your-username/airbnb-console.git


2. Navigate to the project directory:
cd airbnb-console

3. Run the console using the Python interpreter:
python console.py


### How to Use the Command Interpreter

Once the command interpreter is running, you can interact with it using the following commands:

- `help`: Display a list of available commands and their descriptions.
- `create <classname>`: Create a new instance of the specified class (e.g., `User`, `Place`, `Review`).
- `show <classname> <id>`: Display detailed information about a specific instance.
- `all [classname]`: Display a list of all instances of the specified class, or all classes if no argument is provided.
- `update <classname> <id> <attribute> <value>`: Update an attribute of a specific instance.

Here's an example of how to use the command interpreter:

```sh
$ python console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  create  destroy  help  quit  show  update

(hbnb) create User
c7443563-daa4-45d5-aa30-6e7e3fd8d003
(hbnb) show User c7443563-daa4-45d5-aa30-6e7e3fd8d003
[User] (c7443563-daa4-45d5-aa30-6e7e3fd8d003) {'id': 'c7443563-daa4-45d5-aa30-6e7e3fd8d003', 'created_at': datetime.datetime(2023, 8, 7, 10, 0, 0, 1000), 'updated_at': datetime.datetime(2023, 8, 7, 10, 0, 0, 1000)}
