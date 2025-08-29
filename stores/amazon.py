import asyncio
import random
import sys
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from botConfig import amazon_xPaths, additional_settings

#initiates chrome so that the bot can navigate to the product page
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)

#A random delay is necessary in between actions to stimulate human
#actions and not trigger anti bot defense measures on websites
#during website navigation
def random_wait_time():
    wait_time=random.uniform(1.0,5.0)
    time.sleep(wait_time)

#a item is in stock if the add to cart button exists otherwise it is out
#of stock
def check_in_stock(item_link,driver):
    try:
        driver.get(item_link)
        add_to_cart_button = driver.find_element(amazon_xPaths["addToCart"]).click()
        print("Item Found")
        return True
    except NoSuchElementException:
        print("Item not in stock")
        return False

#the desired item is in stock navigate through the checkout process
def purchase_item(item_link,driver):
    deny_warranty = driver.find_element(amazon_xPaths["noWarranty"]).click()
    random_wait_time()
    goto_cart = driver.find_element(amazon_xPaths["goToCart"]).click()
    random_wait_time()
    proceed_checkout = driver.find_element(amazon_xPaths["proceedCheckout"]).click()
    random_wait_time()
    cont_checkout = driver.find_element(amazon_xPaths["continueCheckout"]).click()
    random_wait_time()
    if additional_settings["prime"] == 'False':
        deny_prime = driver.find_element(amazon_xPaths["denyPrime"]).click()
        random_wait_time()
    place_order = driver.find_element(amazon_xPaths["placeOrder"]).click()

#main method that repeats the buying process until the item is successfully
#bought or program is stopped
#the bot will repeat the process every 5-15 minutes to not overwhelm site
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


