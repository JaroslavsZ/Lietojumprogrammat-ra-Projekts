import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

import pyperclip

import os

#Create a directory named Decks
directory_name = "Decks"
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options = option)

with open('deckSource.txt') as f:
    lines = f.readlines()

count = 0

for line in lines:
    count = count + 1
    print(line)
    url = line
    driver.get(url)
    time.sleep(3)

    find = driver.find_element(By.LINK_TEXT, "Download")
    print(find)
    find.send_keys("\n")
    time.sleep(2)

    find = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[2]/button[3]")
    print(find)
    find.send_keys("\n")
    time.sleep(1)

    deck = pyperclip.paste()

    file_path = os.path.join(directory_name, f"{count}.txt")

    with open(file_path, 'w') as file:
        file.write(deck)

    print(str(count) + "/" + str(len(lines)))
    # f = open("decks/" + str(count) + ".txt", "w")
    # f.write(deck)
    # f.close

input()