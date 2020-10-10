# 영화 순위, 제목, 별점 웹스크래핑하기

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만들어 줍니다.

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

# #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
movies = soup.select('#old_content>table>tbody>tr')
# print(movies)

for movie in movies:

    a_tag = movie.select_one('td.title > div > a')

    # a_tag의 유무로 빈 tr과 찾을 tr 거르기
    if a_tag is not None:

        # text 가져오기 --> .text
        # 속성값 가져오기 --> ['속성명']  ex) ['alt']

        # 순위 추출: #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
        # print(movie.select_one('td:nth-child(1) > img')['alt'])
        rank = movie.select_one('td:nth-child(1) > img')['alt']

        # title 추출: #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
        # print(a_tag.text)
        title = a_tag.text

        # 평점 추출: #old_content > table > tbody > tr:nth-child(2) > td.point
        # print(movie.select_one('td.point'))
        star = movie.select_one('td.point').text
        # print(rank, title, star)

        # < 영화 리스트 mongo db에 넣기 >
        # 1. dictionary 형태로 자료 바꿔주기
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }

        # for문을 통해 하나씩 db에 insert 해주기
        db.movies.insert_one(doc)
        # print(doc)

