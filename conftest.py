# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.remote.webdriver import WebDriver


# @pytest.fixture
# def driver() -> WebDriver:
#     options = Options()
#     options.add_argument("--headless=new")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")

#     driver = webdriver.Remote(
#         command_executor="http://chrome:4444/wd/hub",
#         options=options,
#     )
#     yield driver
#     driver.quit()
