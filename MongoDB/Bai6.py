#import
from pymongo import MongoClient
from datetime import datetime
#bước 1: kết nối tới mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client['Drive_Management']
#bước 2:tạo collection
files_collection = db['files']
#bước 3: thêm dữ liệu vào bộ sưu tập
files_data = [
    {'file_id': 1, 'name': "Report.pdf", 'size': 2048, 'owner': "Nguyen Van A", 'created_at': 'datetime("2024-01-10")','shared': 'false'},
    {'file_id': 2, 'name': "Presentation.pptx", 'size': 5120, 'owner': "Tran Thi B", 'created_at': 'datetime("2024-01-15")', 'shared': 'true'},
    {'file_id': 3, 'name': "Image.png", 'size': 1024, 'owner': "Le Van C", 'created_at': 'datetime("2024-01-20")', 'shared': 'false'},
    {'file_id': 4, 'name': "Spreadsheet.xlsx", 'size': 3072, 'owner': "Pham Van D", 'created_at': 'datetime("2024-01-25")', 'shared': 'true'},
    {'file_id': 5, 'name': "Notes.txt", 'size': 512, 'owner': "Nguyen Thi E", 'created_at': 'datetime("2024-01-30")', 'shared': 'false'}
]
files_collection.insert_many(files_data)
#Bước 4: truy vấn
#4.1: xem tất cả các tệp trong bộ sưu tập
print("Tất cả tệp: ")
for file in files_collection.find():
    print(file)
#4.2: tìm tệp có kích thước lớn hơn 2000KB
print("\n Tất cả các tệp có kích thước lớn hơn 2000KB là: ")
files = files_collection.find({'size':{'$gt': 2000}})
for file in files:
    print(file)
#4.3: đếm tổng số tệp
files_collection.count_documents({})
#4.4: tìm tất cả tệp được chia sẻ
print("\n Tất cả các tệp được chia sẻ là: ")
for file in files_collection.find({'shared': True}):
    print(file)
#4.5: thống kê số lượng tệp theo chủ sở hữu
print("\n Số lượng tệp theo chủ sở hữu là: ")
for file in files_collection.aggregate([
    {'$group': {'_id': "$owner", 'count': {'$sum': 1}}}
]):
    print(file)
#Bước 5: cập nhật và xóa thông tin
#5.1: cập nhật trạng thái chia sẻ của tệp với file_id = 1 thành true
files_collection.update_one({'file_id': 1}, {'$set': {'shared': True}})
#5.2: xóa tệp với file id = 3
files_collection.delete_one({'file_id': 3})
#Bước 6: xem lại dữ liệu sau khi cập nhật và xóa
print("\n Dữ liệu tệp sau khi cập nhật và xóa: ")
for file in files_collection.find():
    print(file)
#bước 7: câu hỏi bổ sung
#7.1: tìm tất cả tệp của người dùng có tên "nguyen van a"
print("\n Tất cả các tệp của người dùng có tên 'Nguyễn Văn A': ")
for file in files_collection.find({'owner': "Nguyen Van A"}):
    print(file)
#7.2: tìm tệp lớn nhất trong bộ sưu tập
print("\n Tệp lớn nhất trong bộ sưu tập là:")
for file in files_collection.find().sort({'size': -1}).limit(1):
    print(file)
#7.3: tìm số lượng tệp có kích thước nhỏ hơn 1000KB
print("\n Số lượng tệp có kích thước nhỏ hơn 1000KB là: " ,  files_collection.count_documents({'size': {'$lt': 1000}}))
#7.4: Tìm tất cả các tệp được tạo trong tháng 1 năm 2024
print("\n Tất cả tệp được tạo trong tháng 1 năm 2024 là: ")
for file in files_collection.find({
    'created_at': {'$gte': 'datetime("2024-01-01")', '$lt': 'datetime("2024-02-01")'}
}):
    print(file)
#7.5: cập nhật tên tệp với 'File_id' = 4 thành "New Spreadsheet.xlsx"
print("\n Tên tệp sau khi cập nhật: ", files_collection.update_one({'file_id': 4}, {'$set': {'name': "New Spreadsheet.xlsx"}}))
#7.6: Xóa tất cả các tệp có kích thước nhỏ hơn 1000KB
print("\n Dữ liệu tệp sau khi xóa", files_collection.delete_many({'size': {'$lt': 1000}}))
#đóng kết nối
client.close()