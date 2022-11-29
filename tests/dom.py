import lxml,requests, bs4,re
def getDownlink(version):
    url = "https://chromedriver.chromium.org/downloads"
    f = requests.get(url)
    soup = bs4.BeautifulSoup(f.content,'lxml')

    links = soup.find_all('a',{'class':'XqQF9c'})
    filterArr = []
    def check(link):
        print(len(link['class']) )
        if(link ==1):
            return True
        else:
            return False
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
                print(link['href'])
    
    





# def check2(chara):
#     if(chara== 2):
#         return True
#     else:
#         return False
# arr2 = [1,2,3,4,5]
# filter2= filter(check2,arr2)
# print(next(filter2))



