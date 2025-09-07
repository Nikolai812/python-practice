from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time
import os

def enter_text_in_input(driver, input_id, text):
    """
    Locates an input field by ID and enters the specified text.

    Parameters:
    - input_id: The ID of the input field.
    - text: The text to enter into the input field.
    """
    input_field = driver.find_element(By.ID, input_id)
    input_field.clear()  # Clear any existing text
    input_field.send_keys(text)

def click_button_by_id(driver, button_id):
    """
    Locates a button by ID and clicks it.

    Parameters:
    - button_id: The ID of the button.
    """
    button = driver.find_element(By.ID, button_id)
    button.click()



### colab related methods

def run_all():
    body = driver.find_element(By.TAG_NAME, "body")

    # Create an action chain to simulate Ctrl + F9
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys(Keys.F9) \
        .key_up(Keys.CONTROL) \
        .perform()
    #runtime_button = driver.find_element(By.CSS_SELECTOR, "div[id='runtime-menu']")
    #WebDriverWait(driver, 10).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='runtime-menu']"))
    #)
    #runtime_button.click()

    #run_all_item = WebDriverWait(driver, 10).until(
    #    EC.visibility_of_element_located((By.XPATH, "//div[@command='runall']"))
    #)

    # Optionally scroll into view
    # driver.execute_script("arguments[0].scrollIntoView(true);", run_all_item)

    #run_all_item.click()
    #menu_subitem_run_all = driver.find_element(By.CSS_SELECTOR,
     #                                   "div[command='runall'] > div")
    #menu_subitem_run_all.click()
    pass



if __name__ == '__main__':
    # Specify the path to the ChromeDriver executable
    chrome_driver_path = r"C:\Windriver\chromedriver-win64\chromedriver.exe"

    # Set up Chrome options to automatically download files
    chrome_options = Options()
    download_dir =  r"C:\Windriver"
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)


    # Set up the WebDriver with the specified path
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    try:
        # Open the specified URL

        driver.get("https://www.facebook.com")

        driver.get("https://www.facebook.com/groups/1522757981756335/members")
        time.sleep(3)

        # Enter text into jobname

    except BaseException as e:
        print("While running: ", e)

    finally:
        print("this is finally")
        pass
        #Close the browser
        driver.quit()
        print("after quit")