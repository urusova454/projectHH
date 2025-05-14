from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

def parse_html_file(file_path: str) -> BeautifulSoup :
    """Читает и парсит HTML файл"""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_vacancy_links(soup: BeautifulSoup) -> list:
    """Извлекает ссылки на вакансии из HTML"""
    vacancy_links = soup.find_all('a', href=lambda href: href and '/applicant/vacancy_response' in href)
    return vacancy_links

def extract_vacancy_id(url: str) -> str:
    """Извлекает ID вакансии из URL"""
    match = re.search(r"vacancyId=(\d+)", url)
    return match.group(1) if match else None

def extract_vacancy_api_urls(vacancy_links) -> set:
    """Строит API URLs из ссылок на вакансии"""
    urls = set()
    for link in vacancy_links:
        url = link.get('href')
        id_url = extract_vacancy_id(url)
        url_vacancy = f"https://api.hh.ru/vacancies/{id_url}?host=hh.ru"
        urls.add(url_vacancy)
    return urls

def process_vacancies(urls: set) -> list:
    """Обрабатывает вакансии и возвращает структурированные данные"""
    vacancy = []
    for url in urls:
        published_dates = set()
        job_openings = requests.get(url).json()
        published_at = job_openings.get('published_at')
        if published_at in published_dates:
            continue
        published_dates.add(published_at)

        vacancy.append((
            job_openings.get('id', {}),
            job_openings.get('name', {}),
            job_openings.get('salary', {}),
            job_openings.get('address', {}),
            job_openings.get('description', {}),
            url
        ))
    return vacancy
def save_to_excel(vacancy: list):
    """Сохраняет данные в Excel файл"""
    df = pd.DataFrame(vacancy, columns=[
        'id',
        'name',
        'salary',
        'address',
        'description',
        'url'
    ])
    df.to_excel('result.xlsx')

def pars_hh():
    file_path = '../page.html'

    soup = parse_html_file(file_path)
    vacancy_links = extract_vacancy_links(soup)
    urls = extract_vacancy_api_urls(vacancy_links)
    vacancy = process_vacancies(urls)
    save_to_excel(vacancy)

pars_hh()
