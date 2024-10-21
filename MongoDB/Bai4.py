#import
from pymongo import MongoClient
from datetime import datetime
#bước 1: kết nối tới MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['TiktokPy'] #chọn cơ sở dữ liệu tiktok
#bước 2: tạo các colections
users_collection = db['users']
videos_collection = db['video']
#bước 3: Thêm dữ liệu người dùng
users_data = [
    {'user_id': 1, 'username': "user1", 'full_name': "Nguyen Van A", 'followers': 1500, 'following': 200},
    {'user_id': 2, 'username': "user2", 'full_name': "Tran Thi B", 'followers': 2000, 'following': 300},
    {'user_id': 3, 'username': "user3", 'full_name': "Le Van C", 'followers': 500, 'following': 100}
]
users_collection.insert_many(users_data)
#bước 4: Thêm dữ liệu video
videos_data = [
    { 'video_id': 1, 'user_id': 1, 'title': "Video 1", 'views': 10000, 'likes': 500, 'created_at':'datetime(2024,01,01)'},
    { 'video_id': 2, 'user_id': 2, 'title': "Video 2", 'views': 20000, 'likes': 1500, 'created_at': 'datetime(2024,01,05)'},
    { 'video_id': 3, 'user_id': 3, 'title': "Video 3", 'views': 5000, 'likes': 200, 'created_at': 'datetime(2024,01,10)' }
]
videos_collection.insert_many(videos_data)
#bước 5: truy vấn dữ liệu
#5.1 xem tất cả dữ liệu người dùng
print("Tất cả người dùng")
for user in users_collection.find():
    print(user)
#5.2 Tìm video có nhiều người xem nhất
print("Video có nhiều lượt xem nhất")
mosted_viewed_video = videos_collection.find().sort('view', -1).limit(1)
for user in mosted_viewed_video:
    print(user)
#5.3 tìm tất cả video của người dùng có username là user1
print("\n Tất cả video của người dùng 'user1': ")
user_video = videos_collection.find({'user_id': 1})
for video in user_video:
    print(video)
#bước 6: cập nhật dữ liệu
#cập nhật số người theo dõi của người dùng với user_id là 1 lên 2000
users_collection.update_one({'user_id': 1},{'$set':{'followers': 2000}})
#bước 7: xóa video có video_id là 3
videos_collection.delete_one({'video_id': 3})
#bước 8: xem lại dữ liệu sau khi cập nhật và xóa
print("\n Dữ liệu người dùng sau khi cập nhật: ")
for user in users_collection.find():
    print(user)
print("\n Dữ liệu video sau khi xóa: ")
for video in videos_collection.find():
    print(video)
#đóng kết nối
client.close()