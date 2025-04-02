from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
from src.settings import LOGIN_HH, PASSWORD_HH, HH_URL, logger
from src.selectors.xpath import HH
from src.browsers.chrome import Chrome

def main ():
    urls = set()
    vacancy = []

    logger.info("Скрипт запущен.")
    browser = Chrome()
    browser.get(HH_URL)
    browser.max_window()
    browser.delay_browser()

    browser.click_element(HH.BUTTON_INPUT)
    browser.click_element(HH.BUTTON_INPUT_PASSWORD)
    browser.sends_keys(HH.WINDOW_LOGIN, LOGIN_HH)
    browser.sends_keys(HH.WINDOW_PASSWORD, PASSWORD_HH)
    browser.click_element(HH.BUTTON_INPUT_IN_LK)
    browser.click_element(HH.BUTTON_ADVANCED_SEARCH)
    browser.sends_keys(HH.WINDOW_PROF_OR_POST, "python")
    browser.click_element_scroll(HH.BUTTON_CLOSE_REGION)
    browser.sends_keys_scroll(HH.WINDOW_INCOME, "90000")
    browser.click_element_scroll_for_mark_remote(HH.MARK_REMOTE)
    browser.click_element(HH.BUTTON_FIND)
    logger.info("Скрипт окончен")


    soup = BeautifulSoup(browser.page_source(), 'html.parser')

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





if __name__ == "__main__":
    main()





