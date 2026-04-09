from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PythonOrgPage:
    URL = "https://www.python.org/"
    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def title_contains_python(self):
        return "Python" in self.driver.title

    def search(self, keyword: str):
        elem = self.driver.find_element(*self.SEARCH_BOX)
        elem.clear()
        elem.send_keys(keyword)
        elem.send_keys(Keys.RETURN)

    def has_no_results(self):
        return "No results found." in self.driver.page_source