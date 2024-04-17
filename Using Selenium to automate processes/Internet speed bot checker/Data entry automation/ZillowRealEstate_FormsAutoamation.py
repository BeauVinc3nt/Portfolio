import selenium   # Importing selenium for accessing Chrome driver
import requests   # Used to request web data from URL
from bs4 import BeautifulSoup    # Importing beautiful soup to webscrape data
from selenium import webdriver      # Gives access to Chrome driver. This allows for automation of form filling.
from selenium.webdriver.common.by import By
import time as t    

"""
# FORMAT: SCRAPING DATA ON REAL ESTATE (SET PRICING OF RENT, AREA, N.O BEDROOMS ETC.) -> 
ACCESS CHROME DRIVER -> AUTO FILL FORMS 
"""


GOOGLE_FORM_PROPERTY_QUESTIONS_URL = "https://docs.google.com/forms/d/e/1FAIpQLScSixEyVc6R56yC_p7xODH_Qev3L9T86qHZhjxKS2JFeGxEnQ/viewform?usp=sf_link"
ZILLOW_CLONE_WEBSITE_URL = "https://appbrewery.github.io/Zillow-Clone/"

# HEADERS: required contents for the page to load (AGENTS + LANGUAGES)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# REQUESTING FOR DATA FROM ZILLOW CLONE:
response = requests.get(url=ZILLOW_CLONE_WEBSITE_URL, headers=HEADERS)  
data = response.text

# SETTING UP WEBSCRAPING OBJECT:
soup = BeautifulSoup(data, "html.parser")   # Parsing =  extracting components (e.g. tags, attributes, content) to create a structured representation of the document.


# ----------------------- COLLECTING ALL THE LINKS FOR THE PROPERTIES WITHIN THE PARAMETERS SET ----------------------------------

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") # Locating a specific div's anchor tag contents (all links within this parameter) 
all_links = [link["href"] for link in all_link_elements]    # Using list comprehension to check through each row (links) of the 'link elements' div and assign them to a hyperlink value.

# Printing out a console message to report the amount of links found for property.
print(f"There are {len(all_links)} links availiable to individual property listings in total: \n")  
print(all_links)

# -------------------- COLLECTING ALL ADDRESSES OF THE COLLECTED LINKS USING THE "CSS SELECTOR" TO LOCATE DIFFERENT CONTENTS. ------------------------------

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
# Using list comprehension to remove whitespace (strip spacing and separation with '|' symbol)
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]

print(f"\nAfter having been cleaned up, the addresses now look like this {all_addresses}")


# -------------------- COLLECTING LIST OF ALL THE "PRICES" -----------------------------------------------------------------------------------------
all_price_elements = soup.select(".PropertyCardWrapper span")   # Selecting a CSS tag to specify where pricing data is for property.

# Using list comprehension to clear up the prices contents from "/ month" text to just the plain price in "$".
# PARAMS: IF "$" CHARACTER IS DETECTED IN THE PRICE_ELEMENT, PRINT THIS AS A PRICE REMOVING EXCESS TEXT.

all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(all_prices)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# FILLING IN GOOGLE FORM USING SELENIUM.
chrome_options = webdriver.ChromeOptions()  # Setting up driver options (default). Default opens browser without any history, cookies etc.
chrome_options.add_experimental_option("detach", True)  # Detach keeps the browser open once the script is executed.
driver = webdriver.Chrome(options=chrome_options)   # Taking in the default options.

# GRABBING GOOGLE FORM + FORM QUESTION INPUTS:
# Running a 'for' loop for the amount of links there were scraped for properties:
for n in range(len(all_links)):
    driver.get(GOOGLE_FORM_PROPERTY_QUESTIONS_URL)  # Get the link of the google form with questions
    t.sleep(2)

    # Accessing form question contents + storing them as variables:
    address = driver.find_element(by=By.XPATH,
                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    # Sending data from website to google form automating inputs     
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit.click()

# GOOGLE SHEET LINK FOR LIVE DOCUMENTATION:
