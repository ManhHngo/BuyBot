import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)

driver = setup()
received = sys.stdin.read()

#driver.implicitly_wait(10)
#driver.get("https://www.newegg.com/?srsltid=AfmBOooMHuH0O5En4VXiVZoouDv3imB8CYx7YdToq9v8a9_X-kWXik6L")

