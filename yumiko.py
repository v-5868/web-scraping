from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/tomato"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article',class_="crop-info-repeater")

with open('hisahayo.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Paragarap']
    thewriter.writerow(header)

    for list in lists:  
        paragraph = list.find('p', class_="more").text.replace('\n', '')
        
        
        info = [paragraph]
        thewriter.writerow(info)