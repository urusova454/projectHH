from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from settings import LOGIN, PASSWORD

browser = webdriver.Chrome() # Открытие браузера
browser.maximize_window() # Открытие окна браузера на весь экран
browser.implicitly_wait(3)

browser.get("https://omsk.hh.ru/")

time.sleep(5)
## Вход
button_input = browser.find_element(By.XPATH, '//a[@data-qa="login"]') ## Кнопка ВХОД
button_input.click()
time.sleep(5)
button_input_password = browser.find_element(By.XPATH, '//span[@data-qa="expand-login-by-password-text"]') ## Кнопка "Вход по паролю"
button_input_password.click()
window_login = browser.find_element(By.XPATH, '//input[@data-qa="login-input-username"]') ## Окно Логина
window_login.clear()
window_login.send_keys(LOGIN) ## Ввод Логина
window_password = browser.find_element(By.XPATH, '//input[@data-qa="login-input-password"]') ## Окно пароля
window_login.clear()
window_password.send_keys(PASSWORD) ## Ввод пароля
button_input_in_elk = browser.find_element(By.XPATH, '//button[@data-qa="account-login-submit"]') ## Кнопка вход в ЛК
button_input_in_elk.click()
time.sleep(3)
####

## Настройки Расширенного поиска
button_advanced_search = browser.find_element(By.XPATH, '//*[@aria-label="Расширенный поиск"]')
button_advanced_search.click()
time.sleep(3)
browser.close()
