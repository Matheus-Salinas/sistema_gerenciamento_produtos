import os

class Config:
    MYSQL_DB = os.getenv('MYSQL_DB', 'gerenciamento_produtos')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'manager')
    MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')