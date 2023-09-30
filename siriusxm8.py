import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()


driver = webdriver.Chrome()

driver.get("https://player.siriusxm.com/")

sleep(3)
# this is a change
driver.find_element(by=By.XPATH, value='//*[@id="sxm-welcome-wrapper"]/div/div[1]/div[2]/a').click()
sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys("{Username}")
sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys("{Password}")
sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="app-wrap"]/div[2]/app-welcome-page/overlay-container/div/div/access-now/div[1]/div[2]/form/button/span').click()
sleep(6)
driver.get("https://player.siriusxm.com/query")
sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="searchText"]').send_keys("8")
sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="app-wrap"]/navbar-control/nav/ul/li[4]/form/div/sxm-search-dropdown/div/ul[1]/li[1]/button/span[1]/img').click()
sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="app-wrap"]/player-controls/div/ul/sxm-volume/button/img').click()
sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="app-wrap"]/player-controls/div/ul/sxm-volume/div/button').click()
sleep(15)

filename = 'xm80s.json'

with open(filename, 'r+') as file_object:

    tracklist = {}

    while True:
        with open(filename, 'r') as f:
            tracklist = json.load(f)

        try:
            artist = driver.find_element(by=By.XPATH, value='//*[@id="app-wrap"]/player-controls/div/div[1]/program-descriptive-text/button/div/p[2]').text
            track = driver.find_element(by=By.XPATH, value='//*[@id="app-wrap"]/player-controls/div/div[1]/program-descriptive-text/button/div/p[3]').text
            if artist not in tracklist.keys():
                tracklist[artist] = [track]
            elif artist in tracklist.keys():
                if track not in tracklist[artist]:
                    tracklist[artist].append(track)
        except NoSuchElementException:
            pass
        with open(filename, 'w') as f:
            json.dump(tracklist, f)
        print(tracklist)
        sleep(30)


