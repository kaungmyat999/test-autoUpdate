from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, requests, zipfile,os,lxml,requests, bs4,re


def ChromeSetup(driver_path,):
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)
    driver.set_window_position(0,0)
    driver.set_window_size(1024,768)
    return driver
    



def regex_for_classId(article,css_selector):
    return re.findall('^post-+\d+',article.get_attribute(css_selector))

def finder(driver,ClassNames,i):
    try:
        res = driver.find_element(By.CLASS_NAME,ClassNames[i]).find_element(By.CLASS_NAME,'h1').find_element(By.TAG_NAME,'a')
        if(res):
            return res
    except BaseException:
        return False

def clicker(ct):
    print("Element => ",ct)
    ct.click()
    print("\nCLICK\n")

def go_backer(driver,title):
    if(driver.title != title):
        driver.execute_script("window.history.go(-1)")
    print("\nBackward Trigger!!\n")



#YouTube Play Button Finder
def yt_play_btn_finder(driver):
    return driver.find_element(By.CLASS_NAME,'ytp-chrome-controls').find_element(By.CLASS_NAME,'ytp-left-controls').find_element(By.TAG_NAME,'button')

def yt_mute_btn_finder(driver):
    return driver.find_element(By.CLASS_NAME,'ytp-chrome-controls').find_element(By.CLASS_NAME,'ytp-left-controls').find_element(By.TAG_NAME,'span').find_element(By.TAG_NAME,'button')


def scroll_from_an_element(driver,footer_height,y_delta,txt):
    
    while(y_delta < footer_height):
        print("Y_Delta",y_delta)
        print("FH",footer_height)
        ActionChains(driver).scroll_by_amount(0,y_delta).perform()
        time.sleep(5)
        y_delta += y_delta


def getPath(path):
    return path+'/?paged='
        
#Web 3

def main_link_generator(times,link):
    arr = []
    for i in range(times):
        i += 1
        res = link+str(i)
        arr.append(res)
    return arr

def Indivdual_link_Clicker(driver,individual_Links):
    
    currentDimension = driver.get_window_size()

    for link in individual_Links:
        time.sleep(5)
        driver.get(link)
        time.sleep(5)
        footer = driver.find_element(By.ID,'colophon')

        footer_height = footer.location['y']
        scroll_from_an_element(driver,footer_height,currentDimension['height'],"Down")

def IndividualLinkFetcher(driver,individual_Links):
    cardBodies = driver.find_elements(By.CLASS_NAME, "card_title")
    for card in cardBodies:
        link = card.find_element(By.TAG_NAME,'a')
        if(link):
            individual_Links.append(link.get_attribute('href'))

def regEX(input,link):
    res = input.split(link)
    return (re.search("^\d+",res[1])).group(0)
    

def page_link_regexer(inputArr,link):
    return (regEX(inputArr,link))

def check_and_click(element,text):
    if(element):
        if(element.get_attribute('title') == text):
            print("Clicked!")
            element.click()
        else:
            print("Already Running")


def yt_runner(driver,path,timer):
    driver.get(path)
    currentDimension = driver.get_window_size()
    scroll_from_an_element(driver,100000,currentDimension['height'],'Down')

    # Getting Video Links
    video_titles = driver.find_elements(By.ID,'video-title')
    video_links = [i.get_attribute('href') for i in video_titles]
    print(video_links,'\n',len(video_links))

    for i in video_links:
        driver.get(i)
        play_btn =driver.find_element(By.CLASS_NAME,'ytp-play-button')
        mute_btn = driver.find_element(By.CLASS_NAME,'ytp-mute-button')
        
        check_and_click(mute_btn,'Mute (m)')
        check_and_click(play_btn,'Play (k)')
        time.sleep(timer)
def zipper(zipFolerName,zipLib=zipfile):
    path = os.path.join(os.getcwd(),zipFolerName)
    print("zipp file path -> ",path)
    with zipLib.ZipFile(path,'r') as myzip:
        myzip.printdir()
        myzip.extractall()

def downloader(url,zipFolerName):

    response = requests.get(url, stream=True)
    with open(zipFolerName, "wb") as f:
        for chunk in response.iter_content(chunk_size=512):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    zipper(zipFolerName)



def getDownlink(version):
    url = "https://chromedriver.chromium.org/downloads"
    f = requests.get(url)
    soup = bs4.BeautifulSoup(f.content,'lxml')

    links = soup.find_all('a',{'class':'XqQF9c'})
    arr = []
    for link in links:
        if(len(link['class'])==1):
            arr.append(link)
        
    for i in range(3):
        arr.pop(0)
    print(arr[22])
    print(len(arr))
    for link in arr:
        if(link.find('strong')):
            if(version == re.split(' ',link.find('strong').text)[1]):
                if(link['href']):
                    return ('https://chromedriver.storage.googleapis.com/'+version+'/chromedriver_win32.zip')