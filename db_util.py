import psycopg2 as pg

class DatabaseManager:
    """
    This class is used to interact with the Database
    """
    def __init__(self, dbname, user, password, host, port):
        try:
            self.conn = pg.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cursor = self.conn.cursor()
        except pg.Error as e:
            print(f"Error connecting to the database - {e}")
            raise ConnectionError(e)
