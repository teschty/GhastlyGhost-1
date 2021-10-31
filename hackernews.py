#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

data = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(data, "html5lib")

counter = 0
for story, counter in zip(soup.find_all("a", class_="storylink"), range(10)):
    print("~~~~~~~")
    print("{0}. {1.string}".format(counter, story))

print("~~~~~~~")
