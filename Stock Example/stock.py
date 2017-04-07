'''
Author - Neha Modi
Website scrapped - http://www.marketwatch.com/investing/stock/
'''
import requests
import urllib2
from bs4 import BeautifulSoup
import pandas as pd

f = open("names.txt")
i=0
name = []
value = []
for x in f.readlines():
	link = 'http://www.marketwatch.com/investing/stock/' + x.strip()
	#load_page = requests.get(link)
	load_page = urllib2.urlopen(link)
	soup = BeautifulSoup(load_page,'html.parser')
	Company_Name = soup.find(id="instrumentheader")
	name.append(Company_Name.find(id="instrumentname").get_text())
	#print(i,name)
	price = soup.find(class_='pricewrap')
	value.append(price.find(class_='data bgLast').get_text())
	#print(value)
	print(i)
	i = i+1

stock_value = pd.DataFrame({
		"Company_Name" : name,
		"Value($)" : value
		})
print(stock_value)

print ("Below is comapny with stock value greater than 100")
stock_value['Value($)'] = stock_value['Value($)'].convert_objects(convert_numeric=True)	
print(stock_value.loc[stock_value['Value($)'] >= 100])
stock_value.to_csv('muk.csv', sep=',')

