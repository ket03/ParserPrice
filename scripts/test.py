import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

names = []
prices = []
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://myspar.ru/catalog/postnoe-menyu/")

# count_button_more = driver.find_elements(By.CLASS_NAME, "paging__item")
# print(len(count_button_more))