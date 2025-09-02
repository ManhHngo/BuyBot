import asyncio
import random
import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from botConfig import newegg_xPaths, additional_settings

#force pandas to display full output to ensure all data is shown
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#initiate webdriver so that bot can access website url to buy item and collect item data
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)

#initiate random waits in between page acceses during buying process to imitate human
#actions and prevent site anti bot protection from blocking program
def random_wait_time():
    wait_time=random.uniform(1.0,5.0)
    time.sleep(wait_time)

#An item is in stock if the addtocart button exists since it allows you to checkout
#checks to make sure buying is possible
def check_in_stock(item_link,driver):
    try:
        driver.get(item_link)
        add_to_cart_button = driver.find_element(newegg_xPaths["addToCart"]).click()
        print("Item Found")
        return True
    except NoSuchElementException:
        print("Item not in stock")
        return False

#This function breaks down the website url into the individual product containers so
#that it can easily locate key information including the link, price, item name and status
#so that users can easily copy and paste available items for the bot to purchase
def get_list_in_stock(item_link,driver):
    driver.get(item_link)

    #get the page dom -> get list-wrap which contains all the products
    page_dom = BeautifulSoup(driver.page_source,features="html.parser")
    itemContainer = page_dom.find("div", {"class": "list-wrap"})
    items = itemContainer.findAll("div",{"class":"item-cell"})

    # stores item details once all info combined together
    items_processed = []

    for row in items:
        #process each category to make sure valid entry in items
        row_processed=[]
        itemTitle =row.find("a",{"class": "item-title"})
        itemPromoText = row.find("p",{"class":"item-promo"})
        itemPrice = row.find("li", {"class":"price-current"})

        status = "Available"

        if itemPromoText and itemPromoText.text == "OUT OF STOCK":
            status = "Sold Out"

        #check to make sure item title and price are not hidden
        if itemTitle:
            row_processed.append(itemTitle.text)
            strong_tag = itemPrice.find("strong")
            if strong_tag:
                row_processed.append(itemPrice.find("strong").text)
            else: #price is hidden
                row_processed.append("inf")

            row_processed.append(itemTitle.get("href"))
            row_processed.append(status)

        if row_processed:
            items_processed.append(row_processed)

    #convert array into a pandas table for easy readibility
    dataFrame = pd.DataFrame.from_records(items_processed,columns=["Item Title","Item Price","URL", "Status"])
    #remove commas in each price so conversion into int is possible to reduce memory
    dataFrame["Item Price"] = dataFrame["Item Price"].apply(lambda x: x.replace(",",""))
    dataFrame["Item Price"] = pd.to_numeric(dataFrame["Item Price"])

    return dataFrame

#Autamate Purchasing process of item by clicking through all of the buttons required to checkout
#wait time is necessary to load web content and prevent bot detection
def purchase_item(item_link,driver):
    deny_warranty = driver.find_element(newegg_xPaths["noWarranty"]).click()
    random_wait_time()
    proceed_checkout = driver.find_element(newegg_xPaths["proceedCheckout"]).click()
    random_wait_time()
    enter_cvv = driver.find_element(newegg_xPaths["cvv"]).click()
    enter_cvv.send_keys(additional_settings["cvvNum"])
    checkout = driver.find_element(newegg_xPaths["placeOrder"]).click()

#This fucntion filters a pandas table for items that meet criteria <pricre and available
def filter_price(items):
    maxPrice = additional_settings["maxPrice"]
    return items[items["Item Price"] < maxPrice] and (items.Status == "Sold Out")

#main method that setups browser and initiates the bot given settings
#bot won't turn off and continously run until purchase successful or
#program stopped
async def buy(item_link):
    driver = setup()
    if additional_settings["getItemData"] is "True" and additional_settings["monitor"] is "False" :
        item_list=get_list_in_stock(item_link,driver)
        #if you want to filter by instock
        filtered_list = filter_price(item_list)
        print(filtered_list)

    if additional_settings["getItemData"] is "False" and additional_settings["monitor"] is "False":
        is_in_stock = check_in_stock(item_link, driver)
        print(is_in_stock)

    if additional_settings["getItemData"] is "False" and additional_settings["monitor"] is "True":
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


