import time

from utils import *
from spar_parse import parse_spar
from magnit_parse import parse_magnit
from lenta_parse import parse_lenta
from smart_parse import parse_smart

def main():
    options = set_settings()
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 5)
    # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # parse_spar(driver, wait)
    # time.sleep(1)
    parse_magnit(driver, wait)
    time.sleep(1)
    # parse_lenta(driver)
    # time.sleep(1)
    # parse_smart(driver)
    # time.sleep(1)




    # driver.quit()

def set_settings():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument("--disable-extensions")
    # options.add_experimental_option('useAutomationExtension', False)
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--start-maximized")
    return options


if __name__ == "__main__":
    main()