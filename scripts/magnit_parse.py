from utils import *

def parse_magnit(driver):
    names = []
    prices = []
    driver.get(URL_MAGNIT)
    click_button_age_limit(driver)
    time.sleep(1)
    click_button_accept_coookies(driver)
    time.sleep(1)
    click_button_next_page(driver)
    get_price(driver, names, prices)
    write_to_file("magnit", names, prices)

def click_button_age_limit(driver):
    driver.find_element(By.CLASS_NAME, "alcohol__success").click()

def click_button_accept_coookies(driver):
    driver.find_element(By.CLASS_NAME, "cookies__button").click()

def click_button_next_page(driver):
    count = int(driver.find_elements(By.CLASS_NAME, "num")[-1].text)
    print(count)
    for i in range(count - 1):
        driver.find_element(By.CLASS_NAME, "paginate__more").click()
        time.sleep(2)

def get_price(driver, names, prices):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for name in soup.find_all("div", {'class': 'new-card-product__title'}):
        names.append(name.text)
    for price in soup.find_all("div", {'class': 'new-card-product__price-regular'}):
        prices.append(price.text)