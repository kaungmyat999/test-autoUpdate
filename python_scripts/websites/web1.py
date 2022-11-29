
from time import time
from selenium.webdriver.common.by import By
import time
import os,re,requests, sys


  
print("Current Parent Dir => ",sys.path[0])
sys.path.insert(0,(r'c:\Users\kaung\Documents\Projects\JS\python_shell\python_scripts' ))
print("Current Parent Dir => ",sys.path[0])

from supportFuncs import ChromeSetup, go_backer, page_link_regexer, scroll_from_an_element,downloader,getDownlink

def checkFileExist(currentPath, fileName):
    return os.path.exists(os.path.join(currentPath,fileName))


def isWebDriverExist(checkFileExist,version='107.0.5304.62'):
    if(checkFileExist == True):
        return True
    else:
        # chromeDriverURL = r'https://chromedriver.chromium.org/downloads'
        # driver.get(chromeDriverURL)
        link =getDownlink(version)
        print("L => ",link)
        downloader(link,'webdriver.zip')
        # links = driver.find_elements(By.CLASS_NAME,'XqQF9c')
        # for i in range(3):
        #     links.pop(0)

        # OSVERSION = driver.capabilities['browserVersion']
        # for link in links:
        #     if(OSVERSION == re.split(' ',link.firstChild.textContent)[1]):
        #         print("Download Link ", link.href)
        #         downloader(link.href,'webdriver.zip')

def articleIDfinder(driver,ClassNames,i):
    try:
        print("Inside ",ClassNames[i])
        res = driver.find_element(By.ID,ClassNames[i])
        print("REs => ",res)
        if(res):
            return res
    except BaseException:
        return False

#driver_path = r'C:\Users\kaung\Downloads\chromedriver.exe'
    
isWebDriverExist(checkFileExist(os.getcwd(),'chromedriver.exe'),'108.0.5359.22')
driver_path = os.path.join(os.getcwd(),'chromedriver.exe')

try:
    driver = ChromeSetup(driver_path)

    print("Browers version => ",driver.capabilities['browserVersion'])
except Exception as err:
    
    OSVERSION  = re.search('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*',str(err)).group(0)
    print("OS VERSION -> ",OSVERSION)
    isWebDriverExist(checkFileExist(os.getcwd(),'chromedriver'+OSVERSION+'.exe'),OSVERSION)

driver = ChromeSetup(driver_path)



# path = "https://pyithubawa.com"
# driver.get(path)
# currentDimension = driver.get_window_size()


# mainLinks = []
# link = 'https://pyithubawa.com/?paged='
# def main_link_generator(times,link):
#     for i in range(times):
#         i += 1
#         res = link+str(i)
#         mainLinks.append(res)
#     print("Main_Links => ", mainLinks,'\n')


# hrefArr = []
def Indivdual_link_Fetcher():
    time.sleep(2)
    cardBodies = driver.find_element(By.CLASS_NAME, "fairy-content-area")
    articles = cardBodies.find_elements(By.TAG_NAME,'article')
    time.sleep(1)
    for i in articles:
        cd = (i.find_element(By.CLASS_NAME,'card_body'))
        if(cd):
            h2 = cd.find_element(By.TAG_NAME,'h2')
            if(h2):
                a = h2.find_element(By.TAG_NAME,'a')
                if(a):
                    hrefArr.append(a.get_attribute('href'))

def Indivdual_link_Clicker():
    footer =  driver.find_element(By.TAG_NAME,'footer')

    footer_height = footer.location['y']

    for link in hrefArr:
        time.sleep(5)
        driver.get(link)
        time.sleep(5)
        scroll_from_an_element(driver,footer_height,currentDimension['height'],"Down")


#Looping Pages 

def getTotalPageNumber(link):
    page_link = []
    pg_nums = driver.find_elements(By.CLASS_NAME,'page-numbers')
    for pg in pg_nums:
        page_link.append(pg.get_attribute('href'))
    print("Page Link => ",page_link)
    page_link = page_link[(len(page_link)-2)]
    return page_link_regexer(page_link,link)


    
def run():
    main_link_generator(int(getTotalPageNumber(link)),link)

    try:
        for page in mainLinks:
            driver.get(page)
            currentDimension = driver.get_window_size()
            
            time.sleep(4)
            #Before Fetch All the Individual links from Every Page to hrefArr
            Indivdual_link_Fetcher()
            print(len(hrefArr))

        Indivdual_link_Clicker()
    except Exception as e:
        if(e):
            run()


# run()


    

