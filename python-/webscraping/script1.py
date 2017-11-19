import requests
from bs4 import BeautifulSoup

r = requests.get("https://parents.ebnet.org/genesis/parents?tab1=studentdata&tab2=documents&studentid=25056&action=form")

c=r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class":"cities"})


for item in all:
	print((item.find_all("h2")[0].text) + ": " + (item.find_all("p")[0].text))