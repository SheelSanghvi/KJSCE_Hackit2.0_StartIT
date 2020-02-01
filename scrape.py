import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def GetInfo():
	url = 'https://www.startupindia.gov.in/content/sih/en/search.html?roles=Startup&page=0'
	browser = webdriver.Firefox()
	# url = 'http://winevibe.com/glossary/'
	browser.get(url)
	time.sleep(1)  # wait 20 seconds for the site to load.
	html = browser.page_source
	#page = requests.get("https://www.startupindia.gov.in/content/sih/en/search.html?roles=Startup&page=2")
	#soup = BeautifulSoup(page.content, 'html.parser')
	soup = BeautifulSoup(html, features='html.parser')
	cards=soup.find_all('div', class_='col-md-4')
	#print(cards)
	#print("\n\n\n")
	list1=[]
	for i in range(0,5):
		dict1={}
		name=(cards[i].find_all('h3')[0]).get_text()
		stage=(cards[i].find_all('span',class_='highlighted-text'))[0].get_text()
		location="".join((cards[i].find_all('li',class_='location'))[0].get_text().split())
		filters=(cards[i].find_all('span',class_='dept'))[0].get_text().strip()
		image = cards[i].findAll('img')[0]
		rating=(cards[i].find_all('strong'))[0].get_text()
		#print(image['src'])
		dict1['name']=name
		dict1['stage']=stage
		dict1['location']=location
		dict1['filters']=filters
		dict1['image']=image['src']
		dict1['rating']=rating
		list1.append(dict1)
		
	print (list1)
#browser.close()