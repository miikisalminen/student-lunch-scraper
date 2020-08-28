from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.studentlunch.fi/"



def parse():
	menu =[]
	str1 = ""
#	reading and saving html data
	client = urlopen(url)
	html = client.read()
	client.close

	page_soup = soup(html, "html.parser")

	restauranger = page_soup.findAll("div",{"class":"lunch-item"})

	food = page_soup.findAll("td",{"class":"food"})

	for container in restauranger:
		menu.append("\n"+"> **"+container.h2.get_text()+"**")
		foods = container.findAll("td",{"class":"food"})
		for item in foods:
			menu.append("_• "+item.get_text()+"_")

	for ele in menu:
		str1 += ele
		str1 += "\n"
	return(str1.replace("*",""))

