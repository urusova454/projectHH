
# from src.settings import LOGIN, PASSWORD, HH_URL, logger
# from src.selectors.xpath import Xpath
# <<<<<<< Updated upstream
# from parsers.seleniums.chrome import Chrome
# =======
# from src.settings import LOGIN_HH, PASSWORD_HH, HH_URL, logger
# from src.selectors.xpath import HH
# from src.browsers.chrome import Chrome
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from src.parsers.chrome import Chrome


# def main():
#
#
#     logger.info("Скрипт запущен.")
#     browser = Chrome()
#     browser.get(HH_URL)
#     browser.max_window()
#     browser.delay_browser()
#
#     browser.click_element(Xpath.BUTTON_INPUT)
#     browser.click_element(Xpath.BUTTON_INPUT_PASSWORD)
#     browser.sends_keys(Xpath.WINDOW_LOGIN,LOGIN)
#     browser.sends_keys(Xpath.WINDOW_PASSWORD,PASSWORD)
#     browser.click_element(Xpath.BUTTON_INPUT_IN_LK)
#     browser.click_element(Xpath.BUTTON_ADVANCED_SEARCH)
#     browser.sends_keys(Xpath.WINDOW_PROF_OR_POST, "python")
#     browser.click_element_scroll(Xpath.BUTTON_CLOSE_REGION)
#     browser.sends_keys_scroll(Xpath.WINDOW_INCOME, "90000")
#     browser.click_element_scroll_for_mark_remote(Xpath.MARK_REMOTE)
#     browser.click_element(Xpath.BUTTON_FIND)
#     logger.info("Скрипт окончен")
#
# if __name__ == "__main__":
#     main()
