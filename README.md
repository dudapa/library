# Library Backend Project

This project is a simple backend for a library system, written in Python. It leverages the `psycopg2` module to communicate with a PostgreSQL database and is designed using Object-Oriented Programming (OOP) principles.

## Features

- **Database Connection**: Establishes a connection to a PostgreSQL database using `psycopg2`.
- **Data Fetching**: Retrieves data from the database.
- **Data Insertion**: Inserts new data into the database.
- **Transactions**: Manages database transactions for ensuring data integrity.
- **Other Database Operations**: Supports various other operations required to interact with the PostgreSQL database.

## Requirements

- Python 3.x
- `psycopg2` library
- PostgreSQL database

## Installation and Setup

### Clone the Project

To clone this project, run the following command:

```bash
git clone https://github.com/dudapa/library.git
cd library-backend
````

### Setup the Database

1. **Create the Database**:
   
   Ensure you have PostgreSQL installed and running. Create a new database for the project:

   ```sql
   CREATE DATABASE your_db;
   ```
2. ** Create Tables **
   
   Run the create_tables.py script to create the necessary tables in the database:
   
   ```
   python create_talbes.py
   ```
