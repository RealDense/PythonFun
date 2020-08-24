# import requests
# from bs4 import BeautifulSoup

# URL = 'https://www.facebook.com/events/area-51/storm-area-51-they-cant-stop-all-of-us/448435052621047/'

# headers = {
#     "User-Agent": 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# page = requests.get(URL, verify=False, headers=headers)

# soup = BeautifulSoup(page.content, 'html.parser')

# peopleGoing = soup.find(id="reaction_units")

# print(peopleGoing)

from selenium import webdriver
import time
driver = webdriver.Firefox()
while True:
    print(driver.current_url)
    time.sleep(1)
