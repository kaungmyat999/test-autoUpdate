import requests
import zipfile,os
URL = "https://instagram.com/favicon.ico"
url = 'https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_win32.zip'
response = requests.get(url, stream=True)
with open('webdriver.zip', "wb") as f:
    for chunk in response.iter_content(chunk_size=512):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)


path = os.path.join(os.getcwd(),'webdriver.zip')
with zipfile.ZipFile(path,'r') as myzip:
    myzip.printdir()
    myzip.extractall()

