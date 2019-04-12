import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = input("Please enter url_link> ")
driver = webdriver.Firefox(executable_path=r'/home/hermes/Desktop/insta_video_downloader/geckodriver')
driver.get(url)
elementName = driver.find_elements_by_class_name("tWeCl");
src_url = elementName[0].get_attribute("src")

url_link = src_url
urllib.request.urlretrieve(url_link,'video_name.mp4')
driver.close()