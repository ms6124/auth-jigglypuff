import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PW', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'todoappAuth')

    # JWT configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')