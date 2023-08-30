from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

	def __init__(self, driver):
		self.driver = driver
		self.base_url = "https://test-stand.gb.ru"


	def find_element(self, locator, time=10):    # метод поиска элементов, передаем путь, время ожидания
		return WebDriverWait(self.driver, time).until(EC.  presence_of_element_located(locator), message=f'Cant find element by locator {locator}')  # ждать, пока не появится элемент, если не находится, то выходит ошибка Can't find element by locator {locator}

	def get_element_property(self, locator, property):
		element = self.find_element(locator)
		return element.value_of_css_property(property)

	def go_to_site(self):   #метод для открытия сайта
		return self.driver.get(self.base_url)