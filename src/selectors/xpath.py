from selenium.webdriver.common.by import By
from dataclasses import dataclass

@dataclass
class Xpath:
    BUTTON_INPUT = (By.XPATH, '//a[@data-qa="login"]') # Кнопка ВХОД
    BUTTON_INPUT_PASSWORD = (By.XPATH, '//span[@data-qa="expand-login-by-password-text"]') # Кнопка "Вход по паролю"
    WINDOW_LOGIN = (By.XPATH, '//input[@data-qa="login-input-username"]') # Окно Логина
    WINDOW_PASSWORD = (By.XPATH, '//input[@data-qa="login-input-password"]') # Окно пароля
    BUTTON_INPUT_IN_LK = (By.XPATH, '//button[@data-qa="account-login-submit"]')  # Кнопка вход в ЛК
    BUTTON_ADVANCED_SEARCH = (By.XPATH, '//*[@aria-label="Расширенный поиск"]')
    WINDOW_PROF_OR_POST = (By.XPATH,'//input[@data-qa="vacancysearch__keywords-input" and @class="magritte-field___9S8Tw_7-1-17"]')
    BUTTON_CLOSE_REGION = (By.XPATH, '//button[@data-qa="chip-delete-action"]')
    WINDOW_INCOME = (By.XPATH, '//input[@data-qa="advanced-search-salary"]')  ## Окно дохода
    MARK_REMOTE = (By.XPATH, '//input[@data-qa="advanced-search__work_format-item_REMOTE"]')  # знак "Удаленная работа"
    BUTTON_FIND = (By.XPATH, '//button[@data-qa="advanced-search-submit-button"]')