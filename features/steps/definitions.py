from behave import step
from selenium import webdriver

@step('Navigate to Google')
def test(context):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")