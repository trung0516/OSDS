#import
from pymongo import MongoClient
from datetime import datetime
#bước 1: kết nối tới mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client['Facebook_Data']
#bước 2:tạo các collection
users_collection = db['user']
posts_collection = db['posts']
comments_collection = db['comments']
#bước 3: thêm dữ liệu người dùng
users_data = [
    { 'user_id': 1, 'name': "Nguyen Van A", 'email': "a@gmail.com", 'age': 25 },
    { 'user_id': 2, 'name': "Tran Thi B", 'email': "b@gmail.com", 'age': 30 },
    { 'user_id': 3, 'name': "Le Van C", 'email': "c@gmail.com", 'age': 22 }
]
users_collection.insert_many(users_data)
#bước 4: thêm dữ liệu bài đăng
posts_data = [
    { 'post_id': 1, 'user_id': 1, 'content': "Hôm nay thật đẹp trời!", 'created_at': 'datetime("2024,10,01")' },
    { 'post_id': 2, 'user_id': 2, 'content': "Mình vừa xem một bộ phim hay!", 'created_at': 'datetime("2024,10,02")' },
    { 'post_id': 3, 'user_id': 1, 'content': "Chúc mọi người một ngày tốt lành!", 'created_at': 'datetime("2024,10,03")' }
]
posts_collection.insert_many(posts_data)
#bước 5: thêm dữ liệu bình luận
comment_data = [
    {'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Thật tuyệt vời!", 'created_at': 'datetime("2024,10,01")'},
    {'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': "Mình cũng muốn xem bộ phim này!", 'created_at': 'datetime("2024,10,02")'},
    {'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': "Cảm ơn bạn!", 'created_at': 'datetime("2024,10,03")'}
]
comments_collection.insert_many(comment_data)
#bước 6:truy vấn
#6.1 xem tất cả người dùng
print("Tất cả người dùng")
for user in users_collection.find():
    print(user)
#xem tất cả bài đăng của người dùng user_id = 1
print("\n Tất cả bài đăng của người dùng 'user1': ")
user_post = posts_collection.find({'user_id': 1})
for post in user_post:
    print(post)

#xem tất cả bình luận cho bài đăng với post id = 1
print("\n Tất cả bình luận cho bài đăng với 'post_id'= 1: ")
post_comment = comments_collection.find({'post_id': 1})
for post in post_comment:
    print(post)
#Truy vấn người dùng có độ tuổi trên 25
print("\n Người dùng có độ tuổi trên 25")
users_age = users_collection.find({'age':{'$gt': 25}})
for age in users_age:
    print(age)
#truy vấn tất cả bài đăng được tạo trong tháng 10
print("\n Tất cả bài đăng được tạo trong tháng 10: ")
post_create = posts_collection.find({'created_at': {'$gte':'datetime("2024,10,01")','$lt':'datetime("2024,11,01")' }})
for post in post_create:
    print(post)
#Bước 7:cập nhật và xóa dữ liệu
#Cập nhật nội dung bài đăng của người dùng với post_id = 1
posts_collection.update_one({'post_id': 1}, {'$set':{'content': "Hôm nay trời thật đẹp!"}})
#xóa bình luận với comment_id = 2
comments_collection.delete_one({'comment_id': 2})
#bước 8: xem lại dữ liệu sau cập nhật và xóa
print("\n Dữ liệu người dùng sau khi cập nhật: ")
for post in posts_collection.find():
    print(post)
print("\n Dữ liệu video sau khi xóa: ")
for comment in comments_collection.find():
    print(comment)
#đóng kết nối
client.close()
