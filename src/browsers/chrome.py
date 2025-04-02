from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.settings import TIME_WAIT, logger

import time


class Chrome:
    def __init__(self) -> None:
        logger.info("Браузер запущен.")
        self.browser = webdriver.Chrome()

    def get(self,url: str) -> None:
        """
        Переходит по указанному URL в браузере.
        Параметр:
            url: str - URL открываемой страницы
        Returns:
            None: Метод не возвращает значений.
        """
        self.browser.get(url)
        logger.info(f"Ссылка {url} открыта.")

    def click_element(self, locator: tuple[str, str], time_wait: int = TIME_WAIT) -> None:
        """
        Функция сначала находит элемент по locator(XPAth)  и выполняет клик по данному элементу.
        Параметр:
            locator: tuple[str, str] - Локатор элемента в виде кортежа. Пример locator: By.XPATH, '//a[@data-qa="login"]'
            time_wait: int - Время ожидания в секундах.
        Returns:
            None: Метод не возвращает значений.
        """
        element = self.get_element(locator, time_wait)
        element.click()
        time.sleep(1)
        logger.info(f"Элемент {locator[1]} нажат.")

    def click_element_scroll(self, locator: tuple[str, str], time_wait: int = TIME_WAIT) -> None:
        """
        Функция сначала находит элемент по locator(XPAth), прокручивает до него, чтобы он был в видимой области
        и выполняет клик по данному элементу.
        Параметр:
            locator: tuple[str, str] - Локатор элемента в виде кортежа. Пример locator: By.XPATH, '//a[@data-qa="login"]'
            time_wait: int - Время ожидания в секундах.
        Returns:
            None: Метод не возвращает значений.
        """
        element = self.get_element(locator, time_wait)
        self.scroll(element)
        element.click()
        time.sleep(1)
        logger.info(f"Элемент {locator[1]} нажат.")

    def click_element_scroll_for_mark_remote(self, locator: tuple[str, str]) -> None:
        """
       Функция сначала находит элемент по locator(XPAth), прокручивает до него, чтобы он был в видимой области
       и выполняет клик по данному элементу.
       Параметр:
           locator: tuple[str, str] - Локатор элемента в виде кортежа. Пример locator: By.XPATH, '//a[@data-qa="login"]'
       Returns:
           None: Метод не возвращает значений.
       """
        mark_remote = self.browser.find_element(*locator)  # знак "Удаленная работа"
        self.browser.execute_script("arguments[0].scrollIntoView();", mark_remote)
        mark_remote.click()
        logger.info(f"Элемент {locator[1]} нажат.")


    def sends_keys(self, locator: tuple[str, str], text: str, time_wait: int = TIME_WAIT) -> None:
        """
        Данный метод сначала находит элемент по locator(XPAth), далее отправляет указанный текст в этот элемент.
        Параметр:
            locator: tuple[str, str] - Локатор элемента в виде кортежа. Пример locator: By.XPATH, '//a[@data-qa="login"]'
            text: str - Текст, который необходимо отправить locator
            time_wait: int - Время ожидания в секундах.
        Returns:
            None: Метод не возвращает значений.
            """
        element = self.get_element(locator, time_wait)
        element.send_keys(text)
        time.sleep(1)
        logger.info(f"В поле {locator[1]} добавлено значение {text}.")

    def sends_keys_scroll(self, locator: tuple[str, str], text: str, time_wait: int = TIME_WAIT) -> None:
        """
        Данный метод сначала находит элемент по locator(XPAth), далее прокручивает страницу так чтобы данный элемент был в видимой области
        и отправляет указанный текст в этот элемент.
        Параметр:
            locator: tuple[str, str] - Локатор элемента в виде кортежа. Пример locator: By.XPATH, '//a[@data-qa="login"]'
            text: str - Текст, который необходимо отправить locator
            time_wait: int - Время ожидания в секундах.
        Returns:
            None: Метод не возвращает значений.
        """
        element = self.get_element(locator, time_wait)
        self.scroll(element)
        element.send_keys(text)
        time.sleep(1)
        logger.info(f"В поле {locator[1]} добавлено значение {text}.")

    def get_element(self, locator: tuple[str, str], time_wait: int = TIME_WAIT) -> WebElement:
        """
        Данный метод использует неявное ожидание для поиска элемента по указанному locator. Если элемент становится
        кликабельный в указанный промежуток времени, он возвращается
        Параметр:
            locator: tuple[str, str] - Локатор элемента в виде кортежа. Пример locator: By.XPATH, '//a[@data-qa="login"]'
            time_wait: int - Время ожидания в секундах.
        Returns:
            WebElement: Кликабельный элемент на странице.
        """
        element = WebDriverWait(self.browser, time_wait).until(EC.element_to_be_clickable(locator))
        logger.info(f"Элемент {locator[1]} найден.")
        return element

    def scroll(self,element:  WebElement) -> None:
        """
        Данный метод позволяет прокручивать страницу до заданного элемента
        Параметр:
            element: WebElement - Элемент, к которому необходимо прокрутить страницу
        Returns:
            None: Метод не возвращает значений.
        """
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        logger.info(f"Страница прокручена до {element}.")

    def max_window(self) -> None:
        """
        Данный метод позволяет открыть окно браузера на весь монитор
        Returns:
            None: Метод не возвращает значений.
        """
        self.browser.maximize_window()

    def delay_browser(self) -> None:
        """
        Данный метод устанавливает неявное ожидание в секундах открытия браузера
        Returns:
            None: Метод не возвращает значений.
        """
        self.browser.implicitly_wait(3)

    def page_source(self):
        return self.browser.page_source

