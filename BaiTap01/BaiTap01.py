from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re

# I.tao dataframe rong va noi chua link
all_links = []
musician_links = []
d = pd.DataFrame({'name': [], 'year': []})

# chrome_options = Options()
# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--log-level=3")
# chrome_options.add_argument("--window-size=1920x1080")
# II.lay tat ca duong dan de truy cap den painter

driver = webdriver.Chrome()
url = "https://en.wikipedia.org/wiki/Lists_of_musicians#A"
# #mo trang web
# driver.get(url)
try:
    # mo trang web
    driver.get(url)
    # doi khoang chung 3s
    time.sleep(3)
    # lay ra tat ca the ul
    ul_tags = driver.find_elements(By.TAG_NAME, "ul")
    print(len(ul_tags))
    # chon ul thu 22
    ul_painters = ul_tags[21]  # dem tu 0
    # lay tat ca the <li> thuoc ul_painters
    li_tags = ul_painters.find_elements(By.TAG_NAME, "li")
    print(len(li_tags))
    # #tao danh sach cac url
    links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
    for x in links:
        all_links.append(x)
    # tao danh sach cac title
    titles = [tag.find_element(By.XPATH, "//div[contains(@class,'div-col')]").get_attribute("title") for tag in li_tags]

    # #in ra danh sach
    # for link in links:
    #     print(link)

    # in ra danh sach
    # for title in titles:
    #     print(title)
except:
    print("Error!!")
# tat man hinh
driver.quit()
links
# truy cập vô đường link đầu tiên của all_links
artists_driver = webdriver.Chrome()
artists_driver.get(all_links[0])

# dừng khoảng 2s
time.sleep(2)

try:
    # lấy tất cả các the ul của list of acid rock artists
    ul_artists_tags = artists_driver.find_elements(By.TAG_NAME, "ul")
    print(len(ul_artists_tags))

    # chọn ul thứ 25
    ul_artist = ul_artists_tags[24]
    # lấy tất cả link chứa thông tin thuộc artists
    li_artist = ul_artist.find_elements(By.TAG_NAME, "li")
    print(len(li_artist))

    # tạo danh sách các url của artist
    links_artist = [artist_tag.find_element(By.TAG_NAME, "a").get_attribute("href") for artist_tag in li_artist]
    for x in links_artist:
        musician_links.append(x)
except:
    print("Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
artists_driver.quit()
musician_links
# III.Lay thong tin cua nhac si
count = 0
for link in musician_links:
    if (count >= 20):
        break
    count += 1
    print(link)
    try:
        # khoi tao webdriver
        driver = webdriver.Chrome()
        # mo trang
        url = link
        driver.get(url)
        # doi 2s
        time.sleep(2)
        # lay ten nhac si/ban nhac
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""

        # lay năm hoat dong
        try:
            year_element = driver.find_element(By.XPATH,
                                               value='//span[contains(text(),"Years active")]/parent::*/following-sibling::td')
            year = year_element.text

        except:
            year = ""

        # tao dictionary thong tin hoa si
        painter = {'name': name, 'year': year}
        # chuyen doi dictionary thanh dataframe
        painter_df = pd.DataFrame([painter])
        # them thong tin vao df chinh
        d = pd.concat([d, painter_df], ignore_index=True)
        # dong web
        driver.quit()
    except:
        print("Error!!!!!!!!!!!!!!!")
        # IV.In thong tin ra file excel
d
# #dat ten file excel
file_name = "nhacsi.xlsx"
# saving the excel
d.to_excel(file_name)
# # print('DataFrame is written to Excel File successfully.')