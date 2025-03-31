import  requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами
import os            # Для работы с файлами
import pandas as pd  # Для формирования # датафрейма с результатами

URL = "https://api.hh.ru/vacancies?text=python&employment=full&salary=90000&work_format=REMOTE&excluded_text=Senior,DevSecOps"


def text_search():
    response = requests.get(URL).json()
    vacancy = []
    urls = []
    published_dates = set()
    for item in response['items']:
        urls.append( item.get('url', {}))
    for url in range(len(urls)):
        job_openings = requests.get(urls[url]).json()
        published_at = job_openings.get('published_at')
        if published_at not in published_dates:
            published_dates.add(published_at)
            vacancy.append((job_openings.get('id', {}),
                            job_openings.get('name', {}),
                            job_openings.get('area', {}).get('raw'),
                            job_openings.get('employment', {}).get('name'),
                            job_openings.get('alternate_url', {}),
                            job_openings.get('description', {}),
                            job_openings.get('key_skills', {}),
                            job_openings.get('profession_roles', {}).get('name'),
                            published_at,
                            job_openings.get('created_at', {})
                            ))

    df = pd.DataFrame(vacancy, columns=[
                                        'id',
                                        'name',
                                        'address',
                                        'employment',
                                        'alternate_url',
                                        'description',
                                        'key_skills',
                                        'profession_roles',
                                        'published_at',
                                        'created_at'
                                        ])
    df.to_excel('result.xlsx')

text_search()
