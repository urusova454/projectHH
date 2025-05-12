from selenium.webdriver.common.by import By
from dataclasses import dataclass

@dataclass
class Xpath:
    BUTTON_INPUT = (By.XPATH, '//a[@data-qa="login"]') # Кнопка ВХОД
    # BUTTON_INPUT_PASSWORD = (By.XPATH, '//span[@data-qa="expand-login-by-password-text"]') # Кнопка "Вход по паролю"
    # WINDOW_LOGIN = (By.XPATH, '//input[@data-qa="login-input-username"]') # Окно Логина
    # WINDOW_PASSWORD = (By.XPATH, '//input[@data-qa="login-input-password"]') # Окно пароля
    # BUTTON_INPUT_IN_LK = (By.XPATH, '//button[@data-qa="account-login-submit"]')  # Кнопка вход в ЛК
    BUTTON_ADVANCED_SEARCH = (By.XPATH, '//*[@aria-label="Расширенный поиск"]')
    WINDOW_PROF_OR_POST = (By.XPATH,'//*[@data-qa="vacancysearch__keywords-input"]')
    BUTTON_CLOSE_REGION = (By.XPATH, '//button[@data-qa="chip-delete-action"]')
    WINDOW_INCOME = (By.XPATH, '//input[@data-qa="advanced-search-salary"]')  ## Окно дохода
    MARK_REMOTE = (By.XPATH, '//input[@data-qa="advanced-search__work_format-item_REMOTE"]')  # знак "Удаленная работа"
    BUTTON_FIND = (By.XPATH, '//button[@data-qa="advanced-search-submit-button"]')


    BUTTON_SEARCH_JOB = (By.XPATH, '//div[text()="Профиль соискателя"]')  # Поиск работы
    BUTTON_INPUT2 = (By.XPATH, '//button[@data-qa="submit-button"]') # Кнопка входа №2
    BUTTON_EMAIL = (By.XPATH, '//div[text()="Почта"]') # Кнопка "Почта"
    WINDOW_LOGIN = (By.XPATH, '//input[@data-qa="applicant-login-input-email"]') # Окно Логина
    BUTTON_INPUT_PASSWORD = (By.XPATH, '//button[@data-qa = "expand-login-by-password"]') # Кнопка войти с паролем
    WINDOW_PASSWORD = (By.XPATH, "//input[@data-qa = 'applicant-login-input-password']") # Окно пароля
    BUTTON_INPUT3 = (By.XPATH, "//button[@data-qa = 'submit-button']")
    MARK_REMOTE_ZARPLATA = (By.XPATH, '//input[@data-qa="advanced-search__schedule-item_remote"]')
