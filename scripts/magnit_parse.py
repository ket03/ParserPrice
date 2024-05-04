from utils import *

def parse_magnit(driver, wait):
    names = []
    prices = []
    driver.get(URL_MAGNIT)
    click_button_age_limit(wait)
    click_button_accept_coookies(wait)
    click_button_next_page(wait)
    get_price(driver, names, prices)
    write_to_file("magnit", names, prices)

def click_button_age_limit(wait):
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "alcohol__success"))).click()

def click_button_accept_coookies(wait):
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cookies__button"))).click()
#
def click_button_next_page(wait):
    try:
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "paginate__more"))).click()
        click_button_next_page(wait)
    except TimeoutException:
        return

def get_price(driver, names, prices):
    for name in driver.find_elements(By.CSS_SELECTOR, "div.new-card-product__title"):
        names.append(name.text)
    for price in driver.find_elements(By.CSS_SELECTOR, "div.new-card-product__price-regular"):
        prices.append(price.text)
    # for name in soup.find_all("div", {'class': 'new-card-product__title'}):
    #     names.append(name.text)
    # for price in soup.find_all("div", {'class': 'new-card-product__price-regular'}):
    #     prices.append(price.text)