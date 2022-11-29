import sys
sys.path.insert(0,(r'c:\Users\kaung\Documents\Projects\JS\python_shell\python_scripts' ))

from supportFuncs import ChromeSetup,yt_runner

driver_path = r'C:\Users\kaung\Downloads\chromedriver.exe'
driver = ChromeSetup(driver_path)
path = "https://www.youtube.com/c/WECLICK4MM/videos"

yt_runner(driver,path,320)

