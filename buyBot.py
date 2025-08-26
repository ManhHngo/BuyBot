#This file executes the corresponding buy bot given
# a user providede list of product links in productLinks.txt

from stores import (
    amazon,
    bestbuy,
    gamestop,
    microcenter,
    newegg
)

#This function checks whether a link provided in product is valid
# A valid link is one that a corresponding matching store bot exists
def identify_store(url):
    if "bestbuy.com" in url:
        return "bestbuy"
    elif "amazon.com" in url:
        return "amazon"
    elif "newegg.com" in url:
        return "newegg"
    elif "microcenter.com" in url:
        return "microcenter"
    elif "gamestop.com" in url:
        return "gamestop"
    else:
        return None

#executes the corresponding store bot to see if it exists in order to check out
#else the bot will monitor and respond when the item is available
def dispatch_bot(store, url):
    if store == "bestbuy":
        bestbuy.buy(url)
    elif store == "amazon":
        amazon.buy(url)
    elif store == "newegg":
        newegg.buy(url)
    elif store == "microcenter":
        microcenter.buy(url)
    elif store == "gamestop":
        gamestop.buy(url)
    else:
        print(f"Unknown store for URL: {url}")

#Retrieves the desired product links and removes any unnecesary whitespace
# and /n so that a link is interpreted correctly
    def main():
        linkFile = "productLinks.txt"
        with open(linkFile) as linkReader:
            productLinks = [link.strip() for link in linkReader]
            linkReader.close()

        for url in productLinks:
            store = identify_store(url)
            dispatch_bot(store,url)

    if __name__ == "__main__":
        main()