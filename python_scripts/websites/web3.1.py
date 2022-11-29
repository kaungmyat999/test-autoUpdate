import sys
sys.path.insert(0,(r'c:\Users\kaung\Documents\Projects\JS\python_shell\python_scripts' ))

from collections import deque
from pickle import NONE
from supportFuncs import ChromeSetup, Indivdual_link_Clicker, IndividualLinkFetcher, getPath, go_backer, main_link_generator, scroll_from_an_element
from argparse import Action
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
import time


driver_path = r'C:\Users\kaung\Downloads\chromedriver.exe'
driver = ChromeSetup(driver_path)

path = "https://asonethat.com"
driver.get(path)
individual_Links = []


mainLinks = []
link = getPath(path)


def run():

    mainLinks = main_link_generator(1,link)
    print(mainLinks)

    for page in mainLinks:
        time.sleep(3)
        driver.get(page)
        time.sleep(5)
        IndividualLinkFetcher(driver,individual_Links)
        print(len(individual_Links))
    
    Indivdual_link_Clicker(driver,individual_Links)

run()