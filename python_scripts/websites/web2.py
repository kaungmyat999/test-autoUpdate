import sys
sys.path.insert(0,(r'c:\Users\kaung\Documents\Projects\JS\python_shell\python_scripts' ))

from collections import deque
from pickle import NONE
from supportFuncs import ChromeSetup, getPath, go_backer, page_link_regexer, regEX, scroll_from_an_element
from argparse import Action
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.relative_locator import locate_with
import time


driver_path = r'C:\Users\kaung\Downloads\chromedriver.exe'
driver = ChromeSetup(driver_path)

path = "https://weclick4pdf.com/category/lifestyle/"
driver.get(path)
individual_Links = []

    
def getTotalPageNumber(link):
    page_link = []
    pg_nums = driver.find_elements(By.CLASS_NAME,'page-numbers')
    for pg in pg_nums:
        if(pg.get_attribute('href')):
            page_link.append(pg.get_attribute('href'))
    #page_link = page_link[(len(page_link)-2)]
    return page_link_regexer(page_link,link)
    
       
def IndividualLinkFetcher():
    cardBodies = driver.find_elements(By.CLASS_NAME, "card")

    for card in cardBodies:
        post = card.find_element(By.CLASS_NAME,'post_thumb')
        if(post):
            link = post.find_element(By.TAG_NAME,'a')
            if(link):
                individual_Links.append(link.get_attribute('href'))

mainLinks = []
link = getPath(path)
def main_link_generator(times,link):
    
    for i in range(times):
        i += 1
        res = link+str(i)
        mainLinks.append(res)


def Indivdual_link_Clicker(individual_Link):
    currentDimension = driver.get_window_size()

    for link in individual_Link:
        time.sleep(5)
        driver.get(link)
        time.sleep(5)
        footer = driver.find_element(By.TAG_NAME,'footer')

        footer_height = footer.location['y']
        scroll_from_an_element(driver,footer_height,currentDimension['height'],"Down")



def getTotalPg(PageLinks):
    pgs = driver.find_elements(By.CLASS_NAME, "page-numbers")
    for i in pgs:
        if(i.get_attribute('href')):
            PageLinks.append(i.get_attribute('href'))
    return PageLinks

def getPostLinks(IndividualLinks):

    posts = driver.find_elements(By.CLASS_NAME,'grid-base-post')
    print("P - > ",posts)
    for post in posts:
        link = post.find_element(By.TAG_NAME,'a').get_attribute('href')
        IndividualLinks.append(link)
    return IndividualLinks


def run():
    PageLinks = []
    getTotalPg(PageLinks)
    IndividualLinks = []
    getPostLinks(IndividualLinks)
    PageLinks.pop()
    print(PageLinks)
    print(len(IndividualLinks))
    time.sleep(6)
    for link in PageLinks:
        print("L -> ",link)
        driver.get(link)
        getPostLinks(IndividualLinks)
    print(len(IndividualLinks))
    time.sleep(2)
    Indivdual_link_Clicker(IndividualLinks)

    
    # main_link_generator(int(getTotalPageNumber(link)),link)
    # print(mainLinks)

    # for page in mainLinks:
    #     time.sleep(3)
    #     driver.get(page)
    #     time.sleep(5)
    #     IndividualLinkFetcher()
    #     print(len(individual_Links))
    
    # Indivdual_link_Clicker()


run()

                


