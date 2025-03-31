import requests
import json
from src.domain.vacancies import GeneralVacancy, Vacancy


def parse_items(data: dict) -> list[dict]:
    return data.get("items")

def get_response(url: str) -> dict:
    response = requests.get(url)
    response_data = response.content.decode()
    response.close()
    data_json = json.loads(response_data)
    return data_json

def get_general_vacancies(data: dict) -> list[GeneralVacancy]:
    general_vacancies = []
    general_vacancies_response = parse_items(data)
    for general_vacancy_json in general_vacancies_response:
        general_vacancy_model = GeneralVacancy(**general_vacancy_json)
        general_vacancies.append(general_vacancy_model)

    return general_vacancies

base_url = "https://api.hh.ru/vacancies"
vacancies = []

for page in range(0, 10):
    general_vacancies_response = get_response(f"{base_url}?page={page}&text=python")
    general_vacancies = get_general_vacancies(general_vacancies_response)


    for general_vacancy in general_vacancies:
        vacancy_response = get_response(str(general_vacancy.url))
        vacancy = Vacancy(**vacancy_response)
        vacancies.append(vacancy)
        break

    break


for v in vacancies:
    print(v.name)
