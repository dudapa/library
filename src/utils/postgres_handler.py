import psycopg2
import psycopg2.extras
import traceback
from psycopg2 import sql


class PostgresHandler:
    def __init__(self, host, database, user, password, debug=True):
        self.connection=None
        self.host=host
        self.database=database
        self.user=user
        self.password=password
        self.debug=debug

    def connect(self):
        self.connection=psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        if self.debug:
            print("Connected")

    def insert_data(self, table_name, data_dict):
        if self.connection == None or self.connection.closed:
            self.connect()
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                insert_query = sql.SQL(
                    """
                    INSERT INTO {} ({})
                    VALUES ({})
                    RETURNING *;
                    """
                ).format(
                    sql.Identifier(table_name),
                    sql.SQL(",").join(map(sql.Identifier, data_dict.keys())),
                    sql.SQL(",").join(map(sql.Literal, data_dict.values()))
                )
                if self.debug:
                    print(insert_query.as_string(cursor))
                cursor.execute(insert_query)
                inserted_data = cursor.fetchone()
            except Exception as e:
               traceback.print_exc()
               print(f"Error during inserted_data {e}")
               self.connection.rollback()
            
        self.connection.close()
        return inserted_data

    def get_all_data(self, table_name):
        result = []
        if self.connection == None or self.connection.closed:
            self.connect()
        
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                get_all_query = sql.SQL(
                    """
                    SELECT *
                    FROM {}
                    """
                ).format(
                    sql.Identifier(table_name)
                )
                if self.debug:
                    print(get_all_query.as_string(cursor))
                cursor.execute(get_all_query)
                result = cursor.fetchall()
            except Exception as e:
                traceback.print_exc()
                print(f"Error during getting data {e}")
        
        self.connection.close()
        return result

    def get_selected_data(self, table_name,  target_column, target_value, columns=[]):
        result = []
        if self.connection == None or self.connection.closed:
            self.connect()
        
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                selected_data_query = sql.SQL(
                    """
                    SELECT {}
                    FROM {}
                    WHERE {} = {}
                    """
                ).format(
                sql.SQL(",").join(map(sql.Identifier, columns)),
                sql.Identifier(table_name),
                sql.Identifier(target_column),
                sql.Literal(target_value) 
                )
                if self.debug:
                    print(selected_data_query.as_string(cursor))
                cursor.execute(selected_data_query)
                result = cursor.fetchall()
            except Exception as e:
                traceback.print_exc()
                print(f"Error during getting data {e}")
            
        self.connection.close()
        return result

# TRANSACTIONS
    def borrow_book(self, borrower_id, book_id):
        if self.connection == None or self.connection.closed:
            self.connect()
        
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                transaction_query = sql.SQL(
                    """
                    BEGIN TRANSACTION;

                    UPDATE books
                    SET book_count = (book_count - 1)
                    WHERE book_id = {};

                    INSERT INTO borrows (borrower_id, book_id, borrow_date)
                    VALUES ({}, {}, CURRENT_DATE);

                    COMMIT TRANSACTION;
                    """
                ).format(
                    sql.Literal(book_id),
                    sql.Literal(borrower_id),
                    sql.Literal(book_id)
                )
                if self.debug:
                    print(transaction_query.as_string(cursor))
                cursor.execute(transaction_query)
            except Exception as e:
                print("This book already this borrower read!")
                traceback.print_exc()
                print(f"Error during transaction {e}")
                self.connection.rollback()
            
        self.connection.close()
        return True

    def return_book(self, book_id):
        if self.connection == None or self.connection.closed:
            self.connect()
        
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                transaction_query = sql.SQL(
                    """
                    BEGIN TRANSACTION;

                    UPDATE books
                    SET book_count = book_count + 1
                    WHERE book_id = {};

                    UPDATE borrows
                    SET return_date = CURRENT_DATE
                    WHERE book_id = {};

                    COMMIT TRANSACTION;
                    """
                ).format(
                    sql.Literal(book_id),
                    sql.Literal(book_id)
                )
                if self.debug:
                    print(transaction_query.as_string(cursor))
                cursor.execute(transaction_query)
            except Exception as e:
                traceback.print_exc()
                print(f"Error during transaction {e}")
                self.connection.rollback()
            
        self.connection.close()
        return True

    # JOINING TABLES
    def join_tables(self, tables: list, condition:tuple=()):
        result = []
        if self.connection == None or self.connection.closed:
            self.connect()

        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                if len(tables) == 2 and not condition:
                    join_query = sql.SQL(
                        """
                        SELECT *
                        FROM {}
                        JOIN {} ON {}.{} = {}.{}
                        """
                    ).format(
                        sql.Identifier(tables[0][0]),
                        sql.Identifier(tables[1][0]),
                        sql.Identifier(tables[0][0]),
                        sql.Identifier(tables[0][1]),
                        sql.Identifier(tables[1][0]),
                        sql.Identifier(tables[1][1]),

                    )
                if len(tables) == 3 and not condition:
                    join_query = sql.SQL(
                        """
                        SELECT *
                        FROM {}
                        JOIN {} ON {}.{} = {}.{}
                        JOIN {} ON {}.{} = {}.{}
                        """
                    ).format(
                        sql.Identifier(tables[0][0]),
                        sql.Identifier(tables[1][0]),
                        sql.Identifier(tables[0][0]),
                        sql.Identifier(tables[0][1]),
                        sql.Identifier(tables[1][0]),
                        sql.Identifier(tables[1][1]),
                        sql.Identifier(tables[2][0]),
                        sql.Identifier(tables[0][0]),
                        sql.Identifier(tables[0][2]),
                        sql.Identifier(tables[2][0]),
                        sql.Identifier(tables[2][1])
                    )
                if len(tables) == 3 and condition:
                    join_query = sql.SQL(
                        """
                        SELECT *
                        FROM {}
                        JOIN {} ON {}.{} = {}.{}
                        JOIN {} ON {}.{} = {}.{}
                        WHERE {}.{} = {}
                        """
                    ).format(
                        sql.Identifier(tables[0][0]),
                        sql.Identifier(tables[1][0]),
                        sql.Identifier(tables[0][0]),
                        sql.Identifier(tables[0][1]),
                        sql.Identifier(tables[1][0]),
                        sql.Identifier(tables[1][1]),
                        sql.Identifier(tables[2][0]),
                        sql.Identifier(tables[0][0]),
                        sql.Identifier(tables[0][2]),
                        sql.Identifier(tables[2][0]),
                        sql.Identifier(tables[2][1]),
                        sql.Identifier(condition[0]),
                        sql.Identifier(condition[1]),
                        sql.Literal(condition[2])
                    )
                if self.debug:
                    print(join_query.as_string(cursor))

                cursor.execute(join_query)
                result = cursor.fetchall()
            except Exception as e:
                traceback.print_exc()
                print(f"Error during joining tables {e}")
            
        self.connection.close()
        return result
        