from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

file_path = 'page.html'
urls = set()
vacancy = []

with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'html.parser')


vacancy_links = soup.find_all('a', href=lambda href: href and '/applicant/vacancy_response' in href)

def extract_vacancy_id(url):
    match = re.search(r"vacancyId=(\d+)", url)
    return match.group(1) if match else None

for link in vacancy_links:
    url = link.get('href')
    id_url = extract_vacancy_id(url)
    url_vacancy = f"https://api.hh.ru/vacancies/{id_url}?host=hh.ru"
    urls.add(url_vacancy)

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
        job_openings.get('area', {}).get('name'),
        job_openings.get('employment', {}).get('name'),
        job_openings.get('alternate_url', {}),
        job_openings.get('description', {}),
        job_openings.get('key_skills', {}),
        job_openings.get('profession_roles', {}).get('name'),
        published_at,
        job_openings.get('created_at', {}),
        url
    ))

df = pd.DataFrame(vacancy, columns=[
    'id',
    'name',
    'City',
    'employment',
    'alternate_url',
    'description',
    'key_skills',
    'profession_roles',
    'published_at',
    'created_at',
    'url'
])
df.to_excel('result.xlsx')


