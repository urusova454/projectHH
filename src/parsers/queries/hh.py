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
def get_salary(vacancy_url):
    job_openings = requests.get(vacancy_url).json()
    salary_data = job_openings.get('salary')
    salary_from = salary_data.get('from_', 0) if salary_data else 0
    return salary_from
def get_vacancy_details(vacancy_url, salary_from):
    job_openings = requests.get(vacancy_url).json()
    vacancy = (
        str(uuid4()),
        job_openings.get('name'),
        salary_from,
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
        salary_from = get_salary(vacancy)
        vacancy_data = get_vacancy_details(vacancy, salary_from)
        save_vacancy(vacancy_repo, vacancy_data)
        break
    connection.close()

if __name__ == '__main__':
    main()