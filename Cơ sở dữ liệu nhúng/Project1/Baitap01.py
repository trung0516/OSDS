from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#khởi tạo web driver
driver = webdriver.Chrome()

#mở trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
driver.get(url)

#đợi khoảng 2s
time.sleep(2)
#lấy tất cả các thẻ
tags = driver.find_elements(By.TAG_NAME, "a")

#tạo ra danh sách các liên kết
links = [tag.get_attribute("href") for tag in tags]

#xuất thông tin
for link in links:
    print(link)

#đóng webdriver
driver.quit()
