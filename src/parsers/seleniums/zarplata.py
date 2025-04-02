from src.settings import LOGIN_ZARPLATA, PASSWORD_ZARPLATA, ZARPLATA_URL, logger
from src.browsers.chrome import Chrome
from src.selectors.xpath import Zaprlata
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


def main():
    urls = set()
    vacancy = []

    logger.info("Скрипт запущен.")
    browser = Chrome()
    browser.get(ZARPLATA_URL)
    browser.max_window()
    browser.delay_browser()

    browser.click_element(Zaprlata.BUTTON_INPUT)
    browser.click_element(Zaprlata.BUTTON_INPUT_PASSWORD)
    browser.sends_keys(Zaprlata.WINDOW_LOGIN, LOGIN_ZARPLATA)
    browser.sends_keys(Zaprlata.WINDOW_PASSWORD, PASSWORD_ZARPLATA)
    browser.click_element(Zaprlata.BUTTON_INPUT_IN_LK)
    browser.click_element(Zaprlata.BUTTON_ADVANCED_SEARCH)
    browser.sends_keys(Zaprlata.WINDOW_PROF_OR_POST, "python")
    browser.click_element_scroll(Zaprlata.BUTTON_CLOSE_REGION)
    browser.sends_keys_scroll(Zaprlata.WINDOW_INCOME, "90000")
    browser.click_element_scroll_for_mark_remote(Zaprlata.MARK_REMOTE)
    browser.click_element(Zaprlata.BUTTON_FIND)
    logger.info("Скрипт окончен")

    soup = BeautifulSoup(browser.page_source(), 'html.parser')

    vacancy_links = soup.find_all('a', href=lambda href: href and '/applicant/vacancy_response' in href)

    def extract_vacancy_id(url):
        match = re.search(r"vacancyId=(\d+)", url)
        return match.group(1) if match else None

    for link in vacancy_links:
        url = link.get('href')
        id_url = extract_vacancy_id(url)
        url_vacancy = f"https://api.zarplata.ru/vacancies/{id_url}?host=hh.ru"
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

if __name__ == "__main__":
    main()