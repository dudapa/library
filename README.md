# Library Backend Project

This project is a simple backend for a library system, written in Python. It leverages the `psycopg2` module to communicate with a PostgreSQL database and is designed using Object-Oriented Programming (OOP) principles.

## Project Structure

- **postgres_handler.py**: This module defines the `PostgresHandler` class, which handles database operations such as connecting to the database, fetching data, inserting data, managing transactions, and other related tasks.

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
