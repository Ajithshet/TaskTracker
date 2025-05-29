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

    def __del__(self): # Destructor to close the connection - Backup method
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def close_all(self):
        """
        This function is to close the open connections
        :return:
        """
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def fetch_main_tasks(self):
        """
        This function fetches all main tasks
        :return: list of tuple
        """
        try:
            sql_query = "SELECT * FROM main_tasks"
            self.cursor.execute(query=sql_query)

            data = self.cursor.fetchall()
            return data
        except pg.Error as e:
            print(f"Error fetching main_tasks - {e}")
            raise ConnectionError(e)

    def fetch_child_tasks(self):
        """
           This function fetches all child tasks
           :return: list of tuple
        """
        try:
            sql_query = "SELECT * FROM child_tasks"
            self.cursor.execute(query=sql_query)

            data = self.cursor.fetchall()
            return data
        except pg.Error as e:
            print(f"Error fetching child tasks - {e}")
            raise ConnectionError(e)
