import requests
from src.domain.vacancy_zarplata import GeneralVacancy, Vacancy
from pprint import pprint
URL = "https://api.zarplata.ru/vacancies?text=Python&salary=90000&schedule=remote"

def get_generals_vacancy():
    response = requests.get(URL).json()
    general_vacancies = []
    for item in response['items']:
        general_vacancy_model = GeneralVacancy(**item)
        general_vacancies.append(general_vacancy_model)
    return general_vacancies

vacancies = []
general_vacancies = get_generals_vacancy()

for vacancy in general_vacancies:
    job_openings = requests.get(vacancy.url).json()
    vacancy_g = Vacancy(**job_openings)
    vacancies.append(vacancy_g)
    break
pprint(vacancies)