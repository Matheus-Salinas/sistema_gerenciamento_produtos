from fastapi import Depends
import mysql.connector
from config import Config

def get_db():
    config = Config()
    conn = mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DB
    )
    try:
        yield conn
    finally:
        conn.close()