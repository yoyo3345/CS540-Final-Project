import os
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
          "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
          "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
          "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
          "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
          "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
          "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

abs_path = 'absolute_path'
os.chdir(abs_path)

for dirs in states:
    for i in range(2000, 2006):
        download_path = abs_path + '\\'+dirs
        prefs = {"download.default_directory": download_path}

        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(
            'path_to_driver', chrome_options=opt)
        driver.implicitly_wait(15)
        try:
            driver.get(
                'https://www.epa.gov/outdoor-air-quality-data/air-quality-index-report')
            driver.implicitly_wait(30)

            driver.find_element_by_id('year').send_keys(str(i))
            time.sleep(1)
            driver.find_element_by_id('state').send_keys(str(dirs))
            driver.find_element_by_id('launch').click()
            driver.find_element_by_id('results')
            driver.find_element_by_link_text(
                'Download CSV (spreadsheet)').click()
            time.sleep(3)
        except TimeoutException:
            print("error occured! TimeoutException\n")
        except NoSuchElementException:
            print("error occured! NoSuchElementException\n")
        finally:
            driver.quit()
