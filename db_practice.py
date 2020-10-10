from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만들어 줍니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 데이터를 생성합니다.
db.wizards.insert_one({'name': '덤블도어', 'age': 116})
db.wizards.insert_one({'name': '맥고나걸', 'age': 85})
db.wizards.insert_one({'name': '스네이프', 'age': 60})
db.wizards.insert_one({'name': '해리', 'age': 40})
db.wizards.insert_one({'name': '허마이오니', 'age': 40})
db.wizards.insert_one({'name': '론', 'age': 40})

# MongoDB에서 find 하기

# MongoDB에서 모든 데이터 보기
# all_users = list(db.users.find({}))
# print(all_users)
#
# for user in all_users:
#     print(user['name'])

# MongoDB에서 특정 조건의 데이터 모두 보기
# same_ages = list(db.users.find({'age': 40}))
#
# for user in same_ages:  # 반복문을 돌며 모든 결과값을 보기
#     print(user)


# user = db.users.find_one({'name': '덤블도어'})
# print(user)

# 그 중 특정 키 값을 빼고 보기
# user = db.users.find_one({'name': '덤블도어'}, {'_id': False})
# print(user)

# MongoDB에서 update 하기

# db.users.update_one({'name':'덤블도어'},{'$set':{'age':19}})

# MongoDB에서 delete 하기
db.users.delete_one({'name':'론'})

print(db.users.find_one({'name':'론'}))

