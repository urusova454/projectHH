import requests  # Для запросов по API
from src.domain.vacancy import GeneralVacancy, Vacancy
from pprint import pprint
URL = "https://api.hh.ru/vacancies?text=python&employment=full&salary=90000&work_format=REMOTE&excluded_text=Senior,DevSecOps"

def get_general_vacancy():
    response = requests.get(URL).json()
    general_vacancies = []
    for item in response['items']:
        general_vacancy_model = GeneralVacancy(**item)
        general_vacancies.append(general_vacancy_model)
    return general_vacancies

vacancies = []
general_vacancies = get_general_vacancy()

for vacancy in general_vacancies:
    job_openings = requests.get(vacancy.url).json()
    vacancy_g = Vacancy(**job_openings)
    vacancies.append(vacancy_g)
    break
pprint(vacancies)

