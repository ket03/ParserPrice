import time

from utils import *
 # name - title-data-card
 # price - price-new __color-price
 # button more  - button-show-more-item

 # пока есть кнопка далее -> парсим 12 -> далее
def parse_smart(driver):
    links = []

    driver.get(URL_SMART_CATALOG)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    get_links(soup, links)
    time.sleep(1)
    print(links)
    get_price(driver, links)

def get_links(soup, links):
    for link in soup.find_all("a", class_="title-catalog-group"):
        links.append(link.get("href"))

def get_price(driver, links):
    for link in links:
        driver.get(URL_SMART + link)
        time.sleep(1)
        if driver.find_element(By.CLASS_NAME, "cookie-banner"):
            driver.find_elements(By.CLASS_NAME, "btn-primary")[3].click()
            time.sleep(1)
        # soup = BeautifulSoup(driver.page_source, "html.parser")
        while driver.find_element(By.CLASS_NAME, "button-show-more-item"):
            driver.find_element(By.CLASS_NAME, "button-text-show-more-item").click()
            time.sleep(1)
    # for name in soup.find_all("span", {'class': 'catalog-tile__name'}):
    #     names.append(name.text)
