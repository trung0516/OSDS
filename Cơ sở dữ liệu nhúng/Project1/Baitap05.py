import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re


#tạo data frame rong
d = pd.DataFrame({'name': [],'birth': [], 'death': [], 'Nationality':[] })

#khởi tạo webdriver
driver = webdriver.Chrome()

#mở trang
url = "https://en.wikipedia.org/wiki/Edvard_Munch"
driver.get(url)

#dợi 2 giây
time.sleep(2)
#lấy tên
try:
    name = driver.find_element(By.TAG_NAME, "h1").text

except:
    name = ""
#lấy ngày sinh
try:
    birth_element = driver.find_element(By.XPATH, "//th[text() = 'Born']/following-sibling::td")
    birth = birth_element.text
    birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
except:
    birth = ""
#lấy ngày mất
try:
    death_element = driver.find_element(By.XPATH, "//th[text() = 'Died']/following-sibling::td")
    death = death_element.text
    death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
except:
    death = ""
#lấy quốc tịch
try:
    Nationality_element = driver.find_element(By.XPATH, "//th[text() = 'Nationality']/following-sibling::td")
    Nationality = Nationality_element.text
except:
    Nationality = ""

#tạo ddictrionarry thông tin của họa sĩ
painter = {'name': name, 'birth': birth, 'death': death, 'Nationality': Nationality}

#chuyển đổi dictionary thành DataFrame
painter_df = pd.DataFrame([painter])

#thêm thông tin vào DF chính
d = pd.concat([d, painter_df], ignore_index= True)

print(d)

#thoát web
driver.quit()
