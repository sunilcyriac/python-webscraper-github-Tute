import requests
from bs4 import BeautifulSoup

#Collect the GitHub page
page = requests.get('https://github.com/trending')
print (page)

#Create a BeautifulSoup Object first

soup = BeautifulSoup (page.text, 'html.parser')

print(soup)
