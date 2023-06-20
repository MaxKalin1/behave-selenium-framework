from behave import step
from selenium import webdriver

@step('Navigate to Google')
def test(context):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    @step('Navigate to Ebay')
    def test(context):
        driver = webdriver.Chrome()
        driver.get("https://www.ebay.com/")