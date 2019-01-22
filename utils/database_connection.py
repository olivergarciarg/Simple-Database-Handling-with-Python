import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Conection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:       # if any of these are not null it means there was an error
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()