import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https://stepik.org/a/104774")
    time.sleep(.5)
    title = driver.title
    print(title)

