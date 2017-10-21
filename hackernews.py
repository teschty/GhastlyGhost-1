from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://news.ycombinator.com/").read().decode('utf-8')
soup = BeautifulSoup(html)

# IF ONLY SOMEONE COULD COMPLETE THIS :(
# AND MAKE IT DISPLAY THE TOP 10 TITLES FROM HACKER NEWS
