import requests  # Для запросов по API
from src.repos.vacancies import VacancyRepository
from src.config.database import get_conn
from uuid import uuid4
URL = "https://api.zarplata.ru/vacancies?text=Python&salary=90000&schedule=remote&excluded_text=Senior,DevSecOps"

def get_general_vacancy():
    response = requests.get(URL).json()
    general_vacancies = []
    for item in response['items']:
        general_vacancies.append(item.get('url'))
    return general_vacancies

def get_vacancy_details(vacancy_url):
    job_openings = requests.get(vacancy_url).json()
    vacancy = (
        str(uuid4()),
        job_openings.get('name'),
        job_openings.get('salary'),
        job_openings.get('address'),
        job_openings.get('description'),
        job_openings.get('employer', {}).get('alternate_url'))
    return vacancy

def save_vacancy(vacancy_repo, vacancy_data):
    return vacancy_repo.create(vacancy_data)

def main():

    general_vacancies = get_general_vacancy()
    connection = next(get_conn())
    vacancy_repo = VacancyRepository(connection)

    for vacancy in general_vacancies:
        vacancy_data = get_vacancy_details(vacancy)
        save_vacancy(vacancy_repo, vacancy_data)
        break
    connection.close()

if __name__ == '__main__':
    main()