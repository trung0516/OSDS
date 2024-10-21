from webbrowser import Error

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#khởi tạo web driver
driver = webdriver.Chrome()
for i in range(65, 91):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"
    try:
        # mở trang

        driver.get(url)

        # đợi khoảng 2s
        time.sleep(2)
        # lấy ra tất cả thẻ ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")

        # chọn thẻ ul thứ 2
        ul_painters = ul_tags[20]  # list start with index 0
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        # tạo ra danh sách các url
        links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]

        titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tags]
        # in ra url
        for link in links:
            print(link)
        # in ra title
        for title in titles:
            print(title)
    except:
        print(Error)


#đóng webdriver
driver.quit()
