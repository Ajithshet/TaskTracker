from dotenv import load_dotenv
import os
from db_util import DatabaseManager
from data_util import DataHandling

load_dotenv()

database = os.getenv("DATABASE_NAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")

db = DatabaseManager(dbname=database, user=user, password=password, host=host, port=port)

tasks = DataHandling.get_complete_task(db.fetch_main_tasks(), db.fetch_child_tasks())

print(tasks)

db.close_all()
