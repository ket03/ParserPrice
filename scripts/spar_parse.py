from utils import *

def parse_spar(driver):
    catalog_links = []
    subcatalog_links = []
    prices = []
    names = []

    driver.get(URL_SPAR_CATALOG)

    click_button_city(driver)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    get_links(soup, catalog_links)
    get_subcatalog(driver, catalog_links, subcatalog_links)

    get_price(driver, subcatalog_links, names, prices)
    write_to_file("spar", names, prices)

def click_button_city(driver):
    driver.find_element(By.CLASS_NAME, "js-city-modal-open").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Казань')]").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "js-city-save").click()

def click_button_time_limit(driver):
    driver.find_element(By.CLASS_NAME, "js-modal-close").click()

def click_button_age_limit(driver):
    driver.find_element(By.CLASS_NAME, "js-18-years-accept").click()

def click_button_next_page(driver):
    count_button_more = driver.find_elements(By.CLASS_NAME, "paging__item")
    for i in range(len(count_button_more) - 1):
        driver.find_element(By.CLASS_NAME, "js-next-page").click()

def get_links(soup, links):
    for link in soup.find_all("a", class_="section-tile__title"):
        links.append(link.get("href"))

def get_subcatalog(driver, catalog_links, subcatalog_links):
    for link in catalog_links:
        driver.get(URL_SPAR + link)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        get_links(soup, subcatalog_links)

def get_price(driver, subcatalog_links, names, prices):
    for link in subcatalog_links:
        time.sleep(1)
        driver.get(URL_SPAR + link)
        time.sleep(1)
        click_button_next_page(driver)
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for name in soup.find_all("span", {'class': 'catalog-tile__name'}):
            names.append(name.text)
        for price in soup.find_all("span", {'class': 'prices__cur'}):
            prices.append(price.text.split('.')[0])


# def does_exist_button(driver):
#     try:
#         driver.find_element(By.CLASS_NAME, "mfp-content")
#         click_buttons(driver)
#     except NoSuchElementException:
#         return 0
#
# def click_buttons(driver):
#     button = which_button(driver)
#     driver.find_element(By.CLASS_NAME, button).click()
#
# def which_button(driver):
#     try:
#         driver.find_element(By.CLASS_NAME, "js-18-years-accept")
#         return "js-18-years-accept"
#     except NoSuchElementException:
#         print("not age limit")
#
#     try:
#         driver.find_element(By.CLASS_NAME, "js-city-confirm-close")
#         return "js-city-confirm-close"
#     except NoSuchElementException:
#         print("not choose city")
#
#     try:
#         driver.find_element(By.CLASS_NAME, "js-modal-close")
#         return "js-modal-close"
#     except NoSuchElementException:
#         print("not time limit")