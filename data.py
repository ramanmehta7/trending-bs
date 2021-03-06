import pymongo
from pymongo import MongoClient

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

URL = "https://www.youtube.com/feed/trending"
driver = webdriver.Firefox()
driver.get(URL)

video_title = []
video_url = []
thumbnail_url = []

tag_list = driver.find_elements_by_tag_name(
    'ytd-expanded-shelf-contents-renderer')
for tag in tag_list:
    title_anchor_tag = tag.find_elements_by_id('video-title')
    thumbnail_img_tag = tag.find_elements_by_id('img')

    for anchor_tag in title_anchor_tag:
        video_title.append(anchor_tag.text)
        video_url.append(anchor_tag.get_attribute('href'))

view_count_list = []
subscribers_count_list = []
channel_name_list = []
channel_thumbnails = []
likes_list = []
dislikes_list = []
video_description_list = []

for i in range(len(video_url)):
    url = video_url[i]
    driver.get(url)

    wait = WebDriverWait(driver, 30)
    try:
        title2 = wait.until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, 'h1.ytd-video-primary-info-renderer yt-formatted-string')))
    except:
        pass

    try:
        video_views_count = wait.until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#count > ytd-video-view-count-renderer > span.view-count.style-scope.ytd-video-view-count-renderer')))
    except:
        pass

    channel_data = driver.find_elements_by_css_selector(
        'ytd-video-secondary-info-renderer ytd-video-owner-renderer yt-formatted-string')

    channel_thumbnail = driver.find_elements_by_css_selector(
        'ytd-video-secondary-info-renderer ytd-video-owner-renderer img')

    video_data = driver.find_elements_by_css_selector(
        'ytd-watch-flexy ytd-video-primary-info-renderer ytd-menu-renderer ytd-toggle-button-renderer a yt-formatted-string')

    try:
        show_more_btn = wait.until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#more > yt-formatted-string')))
        show_more_btn.click()
    except:
        pass

    description = driver.find_element_by_css_selector(
        '#description > yt-formatted-string')

    if len(channel_data) > 1:
        channel_name_list.append(channel_data[0].text)
        subscribers_count_list.append(channel_data[1].text)
    if len(channel_thumbnail) > 0:
        channel_thumbnails.append(channel_thumbnail[0].get_attribute('src'))

    view_count_list.append(video_views_count.text)

    if len(video_data) > 1:
        likes_list.append(video_data[0].text)
        dislikes_list.append(video_data[1].text)

    video_description_list.append(description.text)

# MongoDB
cluster = MongoClient(
    'mongodb+srv://localhost80:pass1234@cluster0.5w2ht.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster["trending"]
collection = db["videos"]

videos_list = []
for i in range(len(video_url)):
    videos = {}
    videos["_id"] = i
    videos["title"] = video_title[i]
    videos["url"] = video_url[i]
    videos["channel_name"] = channel_name_list[i]
    videos["subscribers"] = subscribers_count_list[i]
    videos["views"] = view_count_list[i]
    videos["likes"] = likes_list[i]
    videos["dislikes"] = dislikes_list[i]
    videos["description"] = video_description_list[i]
    videos["channel_thumbnail"] = channel_thumbnails[i]
    videos_list.append(videos)


# MongoDB update database
# Here we have deleted all the documents and inserted the previous documents
# If we try to update the documents, then that would be just an overhead for processing, because we actually
# only want the recent videos to be populated in the database which we actually have,
# so its better to insert them instead of updating them.
collection.delete_many({})
collection.insert_many(videos_list)
