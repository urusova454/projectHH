import os
from dotenv import load_dotenv
from loguru import logger


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
ZARPLATA_URL = "https://omsk.zarplata.ru/"