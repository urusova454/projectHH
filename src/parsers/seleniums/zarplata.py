from src.settings import LOGIN_ZARPLATA, PASSWORD_ZARPLATA, ZARPLATA_URL, logger
from src.selectors.xpath import Xpath
from src.parsers.chrome import Chrome

def main():

    logger.info("Скрипт запущен.")
    browser = Chrome()
    browser.get(ZARPLATA_URL)
    browser.max_window()
    browser.delay_browser()

    browser.click_element(Xpath.BUTTON_INPUT)
    browser.click_element(Xpath.BUTTON_SEARCH_JOB)
    browser.click_element(Xpath.BUTTON_INPUT2)
    browser.click_element(Xpath.BUTTON_EMAIL)
    browser.click_element(Xpath.WINDOW_LOGIN)
    browser.sends_keys(Xpath.WINDOW_LOGIN, LOGIN_ZARPLATA)
    browser.click_element(Xpath.BUTTON_INPUT_PASSWORD)
    browser.sends_keys(Xpath.WINDOW_PASSWORD, PASSWORD_ZARPLATA)
    browser.click_element(Xpath.BUTTON_INPUT2)
    browser.click_element(Xpath.BUTTON_ADVANCED_SEARCH)
    browser.sends_keys(Xpath.WINDOW_PROF_OR_POST, "python")
    browser.click_element_scroll(Xpath.BUTTON_CLOSE_REGION)
    browser.sends_keys_scroll(Xpath.WINDOW_INCOME, "90000")
    browser.click_element_scroll_for_mark_remote(Xpath.MARK_REMOTE_ZARPLATA)
    browser.click_element(Xpath.BUTTON_FIND)
    logger.info("Скрипт окончен")

if __name__ == "__main__":
    main()
