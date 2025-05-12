
import requests  # Для запросов по API
from src.repos.vacancies import VacancyRepository
from src.config.database import get_conn
from uuid import uuid4
URL = "https://api.hh.ru/vacancies?text=python&employment=full&salary=90000&work_format=REMOTE&excluded_text=Senior,DevSecOps"

def get_general_vacancy():
    response = requests.get(URL).json()
    general_vacancies = []
    for item in response['items']:
        general_vacancies.append(item.get('url'))
    return general_vacancies

vacancies = []
general_vacancies = get_general_vacancy()
connection = next(get_conn())
vacancy_repo = VacancyRepository(connection)

for vacancy in general_vacancies:
    job_openings = requests.get(vacancy).json()
    vacancy = (
    str(uuid4()),
    job_openings.get('name'),
    job_openings.get('salary'),
    job_openings.get('address'),
    job_openings.get('description'),
    job_openings.get('employer', {}).get('alternate_url'))

    result = vacancy_repo.create(vacancy)
    break
connection.close()
