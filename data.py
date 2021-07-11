# pip install -U selenium
# https://www.geeksforgeeks.org/how-to-install-selenium-in-python/
# python -m pip install mysql-connector-python
import requests
import mysql.connector
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

URL = "https://www.youtube.com/feed/trending"
driver = webdriver.Firefox()
driver.get(URL)

video_title = []
video_url = []

tag_list = driver.find_elements_by_tag_name(
    'ytd-expanded-shelf-contents-renderer')
for tag in tag_list:
    title_anchor_tag = tag.find_elements_by_id('video-title')

    for anchor_tag in title_anchor_tag:
        video_title.append(anchor_tag.text)
        video_url.append(anchor_tag.get_attribute('href'))

print(len(video_url))

view_count_list = []
subscribers_count_list = []
channel_name_list = []
likes_list = []
dislikes_list = []
video_description_list = []

for i in range(len(video_url)):
    url = video_url[i]
    driver.get(url)

    wait = WebDriverWait(driver, 30)
    title2 = wait.until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, 'h1.ytd-video-primary-info-renderer yt-formatted-string')))
    print("Title : " + title2.text)

    video_views_count = wait.until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, '#count > ytd-video-view-count-renderer > span.view-count.style-scope.ytd-video-view-count-renderer')))

    channel_data = driver.find_elements_by_css_selector(
        'ytd-video-secondary-info-renderer ytd-video-owner-renderer yt-formatted-string ')

    video_data = driver.find_elements_by_css_selector(
        'ytd-watch-flexy ytd-video-primary-info-renderer ytd-menu-renderer ytd-toggle-button-renderer a yt-formatted-string'
    )

    try:
        show_more_btn = wait.until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#more > yt-formatted-string')))
        show_more_btn.click()
    except:
        pass
    description = driver.find_element_by_css_selector('#description > yt-formatted-string')
    
    channel_name_list.append(channel_data[0].text)
    subscribers_count_list.append(channel_data[1].text)
    view_count_list.append(video_views_count.text)
    likes_list.append(video_data[0].text)
    dislikes_list.append(video_data[1].text)
    video_description_list.append(description.text)

print(video_title)
print(video_url)
print(channel_name_list)
print(subscribers_count_list)
print(view_count_list)
print(likes_list)
print(dislikes_list)
print(video_description_list)

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="trending",
#   charset="utf8mb4_unicode_ci",
#   use_unicode=True
# )

# cursor = db.cursor()

# cursor.execute("ALTER DATABASE trending CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;")
# cursor.execute("CREATE TABLE IF NOT EXISTS videos (title TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, description TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, url VARCHAR(256), views VARCHAR(32));")

# # for i in range(len(video_title)):
# #     sql = 'INSERT INTO videos VALUES ("' + video_title[i] + '", "' + description[i] + '",  "' + video_url[i] + '",  "' + view_count[i] + '")'
# #     print(sql)
# #     cursor.execute(sql)
# #     db.commit()
# sql = """INSERT INTO videos VALUES (%s, %s, %s, %s);"""
# sql_items = []
# # for i in range(len(video_url)):
# for i in range(5):
#     sql_items.append((
#         video_title[i].replace("'", "\\'"),
#         video_description_list[i].replace("'", "\\'"),
#         video_url[i],
#         view_count_list[i]
#     ))
# cursor.executemany(sql, sql_items)
# db.commit()

# print(cursor.rowcount, " was inserted.")