import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def login():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://twitter.com/')
    time.sleep(3)
    # Click on the login button
    browser.find_element("xpath", '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]').click()
    print("Please log in to Twitter and then press Enter to continue.")
    input("Press Enter to continue: ")
    # Open world population page in a new tab
    browser.execute_script("window.open('https://www.worldometers.info/world-population/')")
    population(browser)

def population(browser):
    browser.switch_to.window(browser.window_handles[1])
    # Get current world population
    population_element = browser.find_element("xpath", '//*[@id="maincounter-wrap"]/div/span')
    population_text = population_element.text
    print("Population without commas:", population_text)
    population_int = int(population_text.replace(",", ""))
    # Check if population exceeds 7.999 billion
    if population_int < 7999999999:
        check_time(browser, population_element, 1)
    else:
        check_time(browser, population_element, 2)

def check_time(browser, population_element, en):
    # Wait for 10 minutes before posting
    time.sleep(600)
    population_text = population_element.text
    population_int = int(population_text.replace(",", ""))
    if population_int < 7999999999:
        en = 1
    else:
        en = 2
    post(browser, population_text, en)

def post(browser, population_text, en):
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://twitter.com/')
    time.sleep(3)
    if en == 2:
        tweet = f"There are now {population_text} of us! #twitter #8billion #8billionofus"
    else:
        tweet = f"There are now {population_text} humans. #twitter #8billion #8billionofus"
    # Click on the tweet button
    browser.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]').click()
    time.sleep(3)
    # Enter the tweet content
    tweet_input = browser.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
    tweet_input.send_keys(tweet)
    time.sleep(3)
    # Click on the tweet button
    try:
        browser.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div').click()
    except:
        browser.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div[2]').click()
        time.sleep(3)
        browser.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div').click()
    # Repeat the process
    population(browser)

login()
