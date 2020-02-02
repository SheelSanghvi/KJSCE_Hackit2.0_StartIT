import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from . import seeds as newsScrape
from selenium.webdriver.firefox.options import Options



def GetInfo():
	options = Options()
	options.add_argument('--headless')
	url = 'https://www.startupindia.gov.in/content/sih/en/search.html?roles=Startup&page=10'
	browser = webdriver.Firefox(options=options)
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
	news_list = newsScrape.getInfo()
	i=0
	while True:
		dict1={}
		name=(cards[i].find_all('h3')[0]).get_text()
		stage=(cards[i].find_all('span',class_='highlighted-text'))[0].get_text()
		location="".join((cards[i].find_all('li',class_='location'))[0].get_text().split())
		filters=(cards[i].find_all('span',class_='dept'))[0].get_text().strip()
		image = cards[i].findAll('img')[0]
		rating=(cards[i].find_all('strong'))[0].get_text()
		#print(image['src'])
		if image['src'] is not 'etc/designs/invest-india/investindialibs/images/user_default_pic.jpeg':

			dict1['image']=image['src']
			dict1['Name']=name
			dict1['Stage']=stage
			dict1['Location']=location
			dict1['Type']=filters
			dict1['Rating']=rating
			dict1['News']=news_list[i]
			list1.append(dict1)
			i=i+1
		if i>=9:
			break

	
	browser.close()
	return list1