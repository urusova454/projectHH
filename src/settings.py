import os
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

TIME_WAIT = 10
HH_URL = "https://omsk.hh.ru/"