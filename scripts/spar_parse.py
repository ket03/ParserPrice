from utils import *

def parse_spar(driver, wait):
    catalog_links = []
    subcatalog_links = []
    prices = []
    names = []

    driver.get(URL_SPAR_CATALOG)

    click_button_city(driver, wait)
    get_links(driver, catalog_links)
    get_subcatalog(driver, catalog_links, subcatalog_links)
    get_price(driver, subcatalog_links, names, prices)
    write_to_file("spar", names, prices)

def click_button_city(driver, wait):
    driver.find_element(By.CLASS_NAME, "js-city-modal-open").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Казань')]"))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-city-save"))).click()

def click_button_next_page(wait):
    try:
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-next-page"))).click()
        click_button_next_page(wait)
    except TimeoutException:
        return

def click_button_ok(wait):
    try:
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mfp-close"))).click()
    except TimeoutException:
        return

def get_links(driver, links):
    for link in driver.find_elements(By.CSS_SELECTOR, "a.section-tile__title"):
        links.append(link.get_attribute("href"))

def get_subcatalog(driver, catalog_links, subcatalog_links):
    for link in catalog_links:
        driver.get(link)
        get_links(driver, subcatalog_links)

def get_price(driver, subcatalog_links, names, prices):
    wait = WebDriverWait(driver, 1)
    for link in subcatalog_links:
        driver.get(link)
        click_button_ok(wait)
        click_button_next_page(wait)

        for name in driver.find_elements(By.CSS_SELECTOR, "span.catalog-tile__name"):
            names.append(name.text)
        for price in driver.find_elements(By.CSS_SELECTOR, "span.prices__cur"):
            prices.append(price.text)