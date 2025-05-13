import requests  # Для запросов по API
from src.domain.vacancies import Vacancy
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

for vacancy in general_vacancies:
    job_openings = requests.get(vacancy).json()
    id = uuid4()
    name = job_openings.get('name')
    salary = job_openings.get('salary')
    address = job_openings.get('address')
    description = job_openings.get('description')
    url = job_openings.get('employer', {}).get('alternate_url')
    vacancy_g = Vacancy(id = id, name = name, salary = salary, address = address, description = description, url = url)
    break