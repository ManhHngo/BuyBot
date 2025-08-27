#these are the tags corresponding to the buttons needed
#to be pressed on each website to check out
#They are used to tell selenium what to click
#This assumes you are signed in to respective website

newegg_xPaths = {
    "addToCart" : '//*[@id="ProductBuy"]/div[1]/div[2]/button',
    "noWarranty": '//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]',
    "proceedCheckout": '//*[@id="modal-intermediary"]/div/div/div[2]/div[1]/div[3]/button[2]',
    "cvv" : '//*[@id="app"]/div/section/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/label/div/div[4]/input',
    "placeOrder": '//*[@id="Summary_Side"]/div[1]/div[1]/button'
}

amazon_xPaths = {
    "addtoCart" : '//*[@id="add-to-cart-button"]',
    "noWarranty": '//*[@id="attachSiNoCoverage"]/span/input',
    "goToCart" : '//*[@id="ace-gtc"]/span/a',
    "proceedCheckout": '//*[@id="sc-buy-box-ptc-button"]/span/input',
    "continueCheckout": '//*[@id="checkout-primary-continue-button-id"]/span/input',
    "denyPrime": '//*[@id="prime-decline-button"]/span/a/span',
    "placeOrder": '//*[@id="placeOrder"]'
}

bestbuy_xPaths = {
    "addToCart" : '/html/body/div[5]/div[4]/div[2]/div/div[8]/div[1]/div/div/button',
    "checkout": '//*[@id="cartApp"]/div[2]/div/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button',
    "toPayment": '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[3]/div[1]/section/div[3]/section/div/div/button/span',
    "placeOrder": '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[3]/div[2]/div/section/div[2]/div/div[2]/div/button/span'

}

microcenter_xPaths = {
    "addToCart": '//*[@id="options-button"]/div/form/div[1]/button',
    "viewInCart": '//*[@id="cartModal"]/div[1]/div/div[3]/div[1]/a',
    "checkOut": '/html/body/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/button'
}

gamestop_xPaths = {
    "addToCart": '//*[@id="add-to-cart-buttons"]/div[2]/div/button[1]',
    "noWarranty": '//*[@id="addedToCartModal"]/div/div/div[2]/div[2]/button[1]',
    "checkout": '/html/body/div[6]/div[7]/div[1]/div[2]/div[4]/div[5]/div/div[2]/div[1]/div/a/span',
    "placeOrder": '//*[@id="place-order-spc"]/div/div'
}