import asyncio
import random
import sys
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from botConfig import newegg_xPaths, additional_settings

def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)

def random_wait_time():
    wait_time=random.uniform(1.0,5.0)
    time.sleep(wait_time)

def check_in_stock(item_link,driver):
    try:
        driver.get(item_link)
        add_to_cart_button = driver.find_element(newegg_xPaths["addToCart"]).click()
        print("Item Found")
        return True
    except NoSuchElementException:
        print("Item not in stock")
        return False

def purchase_item(item_link,driver):
    deny_warranty = driver.find_element(newegg_xPaths["noWarranty"]).click()
    random_wait_time()
    proceed_checkout = driver.find_element(newegg_xPaths["proceedCheckout"]).click()
    random_wait_time()
    enter_cvv = driver.find_element(newegg_xPaths["cvv"]).click()
    enter_cvv.send_keys(additional_settings["cvvNum"])
    checkout = driver.find_element(newegg_xPaths["placeOrder"]).click()

async def buy(item_link):
    driver = setup()
    is_in_stock = check_in_stock(item_link, driver)
    while True:
        if is_in_stock is True:
            print("Item is in stock: Proceeding to purchase")
            purchase_item(item_link, driver)
            break
        else:
            print("Item still out of stock. Check back later")
            await asyncio.sleep(random.randint(300, 900))

        driver.quit()


