from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://treehouse-projects.githubio.io/horse-land/index.html')

time.sleep(5)

page_html = driver.page_source

soup = BeautifulSoup(page_html, 'html-parser')

print(soup.prettify())

driver.close()
