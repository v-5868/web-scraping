from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.flipkart.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('a', class_="_6WQwDJ T88g6k")

with open('misa.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Price','heading']
    thewriter.writerow(header)

    for list in lists:  
        price = list.find('div', class_="_2tDhp2").text.replace('\n', '')
        heading = list.find('div', class_="_3LU4EM").text.replace('\n', '')
    
        info = [price,heading]
        thewriter.writerow(info)