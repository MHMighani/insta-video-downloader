import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def video_downloader(url):
	driver = webdriver.Firefox(executable_path=r'/home/hermes/Desktop/insta_video_downloader/geckodriver')
	driver.get(url)
	elementName = driver.find_elements_by_class_name("tWeCl");
	src_url = elementName[0].get_attribute("src")
	video_name = (url.split('/'))[4]
	url_link = src_url
	urllib.request.urlretrieve(url_link,video_name + '.mp4')
	driver.close()

url = input("Please enter url_link> ")

video_downloader(url)	

if __name__ == '__main__':
	pass

