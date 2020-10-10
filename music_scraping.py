import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만들어 줍니다.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

# tr목록 selector: #body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
musicList = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# print(musicList)

for music in musicList:
    # 음원순위 selector: # body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
    # print(music.select_one('td.number').text.split(" ")[0])
    rank = music.select_one('td.number').text.split(" ")[0].strip()

    # 음원이름 selector: # body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
    # print(music.select_one('td.info > a.title.ellipsis').text)
    name = music.select_one('td.info > a.title.ellipsis').text.strip()

    # print(rank, name)

    doc = {
        'rank':rank,
        'name':name
    }

    db.musics.insert_one(doc)