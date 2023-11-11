import selenium, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
FORM_URL = "https://forms.gle/XYX43JLL5jxveoPW9"
WEBSITE_URL = "https://appbrewery.github.io/Zillow-Clone/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

bot = webdriver.Chrome(options=chrome_options)

bot.get(WEBSITE_URL)

a_list = bot.find_elements(By.CSS_SELECTOR, ".StyledPropertyCardDataWrapper a")

links = [a.get_attribute("href") for a in a_list]
adress_list = [a.text for a in a_list]
adress_list = [address.replace("|", "") for address in adress_list]
print(adress_list)

price_list = bot.find_elements(By.CSS_SELECTOR, ".PropertyCardWrapper span")
price_list = [price.text.split("+")[0] for price in price_list]
price_list = [price.split("/")[0] for price in price_list]
print(price_list)



bot.get(FORM_URL)
time.sleep(1)
for adres, price, link in zip(adress_list, price_list, links):
    bot.find_elements(By.CSS_SELECTOR, ".KHxj8b ")[0].send_keys(adres)
    bot.find_elements(By.TAG_NAME, "textarea")[1].send_keys(price)
    bot.find_elements(By.TAG_NAME, "textarea")[2].send_keys(link)

    bot.find_element(By.CSS_SELECTOR, ".lRwqcd div span").click()
    time.sleep(0.5)
    bot.get(FORM_URL)
    time.sleep(0.5)

bot.quit()

