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

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

TIME_WAIT = 10
HH_URL = "https://omsk.hh.ru/"