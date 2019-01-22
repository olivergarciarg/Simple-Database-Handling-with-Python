"""
Concerned with storing and retrieving books from a database.
"""
from typing import List, Dict, Union
from .database_connection import DatabaseConnection


Book = Dict[str, Union[str, int]]          # This is new type


def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(name: str, author: str) -> None:            # "name: str" the colon and the value after it are optional, they are used to hint what type of value is name
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))     # SQLITE3 sefaly SCAPES the inserted values, removes injection attacks risks


def get_all_books() -> List[Book]:              # List[Dict[str, str, int]]
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))     # SQLITE3 sefaly SCAPES the inserted values, removes injection attacks risks ---- (name,) makes it a touple


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?', (name,))     # SQLITE3 sefaly SCAPES the inserted values, removes injection attacks risks ---- (name,) makes it a touple

