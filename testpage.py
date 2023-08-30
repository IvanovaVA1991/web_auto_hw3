from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:  # класс для хранения локаторов
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")  # поле логина задаем селектор по xpath
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")  # поле пароля
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')  # задаем селектор по css селектору
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')  # селектор элемента с ошибкой 401 (chrome!)
    LOCATOR_CONTACT = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]')
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_US_BUTTON = (By.XPATH, """//*[@id="contact"]/div[4]""")



class OperationsHelper(BasePage):  # класс OperationsHelper наследуется от BasePage
    def enter_login(self, word):
        #logging.info(f'send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
       # logging.info(f'send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
       # logging.info('Clock login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
       # logging.info(f'We found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        return text

    def click_contact_button(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def click_contact_us_button(self):
        self.find_element(TestSearchLocators.LOCATOR_US_BUTTON).click()

    def enter_name(self, word):
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email(self, word):
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def enter_content(self, word):
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)