import os
from dotenv import load_dotenv
from loguru import logger
from pathlib import Path


# Настройка логирования
logger.add(
    "logs/file.log",
    rotation="1 MB",
    retention="10 days",
    format="{time} {level} {message}",
    level="INFO",
)

load_dotenv()

LOGIN_HH = os.getenv('LOGIN')
PASSWORD_HH = os.getenv('PASSWORD')

TIME_WAIT = 10
HH_URL = "https://omsk.hh.ru/"




HOST = "127.0.0.1"
USER = "postgres"
DBNAME = "hh_db"
PASSWORD = "4023"
PORT = "5432"
BASE_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)
MIGRATION_PATH = BASE_PATH / "repos" / "migrations"
