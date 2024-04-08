# LIBRARIES
import selenium
from selenium.webdriver.common.keys import Keys  # Permission to send through automated inputs (via environ)
from selenium.webdriver.common.by import By     # Importing "By" object to access different elements via selenium. 
from selenium import webdriver      # Grants access to a driver to search the internet + make requests. 
import undetected_chromedriver as uc    # Allows chrome driver go us undetected as an automated browser.
import os    # Allows direct access to local computer's operating system (env variables)
import time as t # Enables a delay between different tasks (bypass bot detection)
from datetime import datetime

# Internet speed contents promised by ISP (Internet Service Provider) used to determine whether internet stats are sent or not:
PROMISED_DOWN = 150 # Promised Upload speed
PROMISED_UP = 30 # promised download speed


TWITTER_EMAIL = os.environ.get('NameOfLocalEnvironmentVariableEmail')
TWITTER_PW = os.environ.get('NameOfLocalEnvironmentVariablePassword')

# Capturing the current time with datetime obj.
CurrentTime = datetime.now()
CurrentDate = CurrentTime.date()

# URLs of speed test (bot grabs data from) + twitter sign in page
SpeedtestURL = "https://www.speedtest.net/" # Website where internet speed tests are ran.
TwitterSignInURL = "https://twitter.com/login"  # twitter sign in page

# Setting up the Twitter bot + its attributes.
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = uc.Chrome(enable_cdp_events=True) # Chrome Devtools Protocol - helps you inspect/ control browser's behaviour.
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.UploadSpeed = int        # Initial values for bot object (values overwritten once found.)
        self.DownloadSpeed = int

    # Method for getting internet speeds.
    def get_internet_speed(self):
        self.driver.get(SpeedtestURL)
        InternetSpeedPageConsent = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")  # Locating HTML element for consent button to click/ bypass bot check 1.
        InternetSpeedPageConsent.click()
        t.sleep(1)  # Adds a 1 second delay between current task -> next task.

        # STEP 2: Clicking on speed test to run upload/ download speeds.
        FindInternetSpeedButton = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        FindInternetSpeedButton.click()
        # CONSOLE OUTPUTS: (this is logged to display to the user the process is running smoothly).
        print("Calculating upload and download speeds... ")
        t.sleep(4)
        print("This may take between 30-60 secs.\n\n")
        t.sleep(40)

        self.DownloadSpeed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text  
        self.UploadSpeed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        
        # ONCE CONDITIONS ARE TRUE (BOTH VALUES HAVE BEEN FOUND):
        print(f"Upload speed:  {self.UploadSpeed} Mbps\nDownload speed:  {self.DownloadSpeed} Mbps")

    # Method for logging into Twitter + sending tweet.
    def TweetProvider(self):
        self.driver.get(TwitterSignInURL) # Bot opening twitter sign up page.
        t.sleep(1)

        # PASSING IN EMAIL + PASSWORD CREDENTIALS FROM ENVIRON.
        Email = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        Email.send_keys(TWITTER_EMAIL, Keys.ENTER)  # PASS IN EMAIL -> ENTER

        t.sleep(2)      # Adds delay between sending email and sending password.

        Password = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input") 
        Password.send_keys(TWITTER_PW, Keys.ENTER)  # PASS IN PASSWORD -> ENTER
        t.sleep(4)

        # Locating the "post button to create a tweet message to distribute via Xpath.
        ComposeTweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        TweetMessage = f"""INTERNET SPEED TEST ({CurrentDate}) :
        \n\nMy internet speeds are: 
        \n- {self.UploadSpeed}Mbps upload speed
        \n- {self.DownloadSpeed}Mbps download speed."""
        ComposeTweet.send_keys(TweetMessage)    # send tweet contents -> posting tweet.

        SendTweetButton = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span")
        SendTweetButton.click()

      # EXCEPTION HANDLING - testing for different outcomes + output appropriate solution. TEST ORDER PRIORITY RANKING: Try -> except
        try:
            print(f"\nSUCCESS! Internet speed test report sent on {TWITTER_EMAIL} at:\n {CurrentTime}.\n")
            self.driver.quit()  # Once bot has scraped successfully tweeted, close the webpage via driver quit.
        except:     # IF ERROR OCCURS -> run exception
            print("Oops! An unknown error has occured. \nWe will run the tests again in just a second...")
            t.sleep(2)
            RunTwitterBotTests()    # ReRunning bot test to push out tweet.


# STEPS BOT TAKES TO SUCCESSFULLY GENERATE TWEET.
# Create SpeedTwitterBot object -> check internet speeds -> write tweet with ISP report -> send tweet with current date of test. )
def RunTwitterBotTests():
    bot = InternetSpeedTwitterBot() 
    bot.get_internet_speed()
    bot.TweetProvider()

RunTwitterBotTests()  # Initialising bot
