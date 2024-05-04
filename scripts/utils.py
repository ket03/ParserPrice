import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

URL_SPAR = "https://myspar.ru"
URL_SPAR_CATALOG = "https://myspar.ru/catalog/"

URL_MAGNIT = "https://magnit.ru/catalog/"

URL_LENTA = "https://lenta.com/catalog/"

URL_SMART = "https://smart.swnn.ru"
URL_SMART_CATALOG = "https://smart.swnn.ru/catalog"

URL_AUCHAN = "https://www.auchan.ru/"

BUTTON_ALCOHOL_MAGNIT = "alcohol__success"
BUTTON_COOKIES_MAGNIT = "cookies__button"
BUTTON_NEXT_PAGE_MAGNIT = "paginate__more"


BUTTON_ALCOHOL_SPAR = "js-18-years-accept"
BUTTON_TIME_LIMIT_SPAR = "js-modal-close"
BUTTON_NEXT_PAGE_SPAR = "js-next-page"



def write_to_file(store, names, prices):
    today = date.today()
    f = open(store + "_" + str(today) + ".txt", "w")

    for name, price in names, prices:
        f.writelines(name + " = " + price)
    f.close()