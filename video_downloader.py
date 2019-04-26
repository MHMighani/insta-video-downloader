import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

current_path = os.path.dirname(os.path.realpath(__file__))
exc_path = current_path + '/geckodriver'


def video_downloader(url):
    driver = webdriver.Firefox(executable_path=r'%s' % exc_path)
    driver.get(url)
    elementName = driver.find_elements_by_class_name("tWeCl")
    src_url = elementName[0].get_attribute("src")
    video_name = (url.split('/'))[4]
    url_link = src_url
    urllib.request.urlretrieve(url_link, video_name + '.mp4')
    driver.close()


def main():
    url = input("Please enter url_link> ")
    video_downloader(url)


if __name__ == '__main__':
    main()
