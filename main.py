
import time
from src.settings import LOGIN, PASSWORD, HH_URL, logger
from src.selectors.xpath import Xpath
from src.browsers.chrome import Chrome

def main():
    logger.info("Скрипт запущен.")
    browser = Chrome()
    browser.get(HH_URL)
    browser.max_window()
    browser.delay_browser()

    browser.click_element(Xpath.BUTTON_INPUT)
    browser.click_element(Xpath.BUTTON_INPUT_PASSWORD)
    browser.sends_keys(Xpath.WINDOW_LOGIN,LOGIN)
    browser.sends_keys(Xpath.WINDOW_PASSWORD,PASSWORD)
    browser.click_element(Xpath.BUTTON_INPUT_IN_LK)
    browser.click_element(Xpath.BUTTON_ADVANCED_SEARCH)
    browser.sends_keys(Xpath.WINDOW_PROF_OR_POST, "python")
    browser.click_element_scroll(Xpath.BUTTON_CLOSE_REGION)
    browser.sends_keys_scroll(Xpath.WINDOW_INCOME, "90000")
    browser.click_element_scroll_for_mark_remote(Xpath.MARK_REMOTE)
    browser.click_element(Xpath.BUTTON_FIND)
    logger.info("Скрипт окончен")
    time.sleep(7)

if __name__ == "__main__":
    main()

#
# mark_remote = browser.find_element(*Xpath.MARK_REMOTE) # знак "Удаленная работа"
# browser.execute_script("arguments[0].scrollIntoView();", mark_remote)
# mark_remote.click()
#



