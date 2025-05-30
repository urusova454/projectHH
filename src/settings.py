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

LOGIN_HH = os.getenv('LOGIN_HH')
PASSWORD_HH = os.getenv('PASSWORD_HH')

LOGIN_ZARPLATA = os.getenv('LOGIN_ZARPLATA')
PASSWORD_ZARPLATA = os.getenv('PASSWORD_ZARPLATA')


TIME_WAIT = 10
HH_URL = "https://omsk.hh.ru/"
ZARPLATA_URL = "https://chelyabinsk.zarplata.ru/"

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_DBNAME = os.getenv("POSTGRES_DBNAME")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")


BASE_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
MIGRATION_PATH = BASE_PATH / "repos" / "migrations"
