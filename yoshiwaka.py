from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.amazon.in/deal/9597af29?showVariations=true&pf_rd_r=EF281RQDDFQNM2BH9MKJ&pf_rd_p=7f4a3afe-60dd-4be9-828c-5703b1b1238a&pd_rd_r=85f1e248-5069-40ca-897e-7ab31e638fed&pd_rd_w=Gc3we&pd_rd_wg=R1Ccv&ref_=pd_gw_unk"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('span', class_="a-list-item")

with open('hisaho.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Price','heading']
    thewriter.writerow(header)

    for list in lists:  
        price = list.find('span', class_="a-price-whole").text.replace('\n', '')
        heading = list.find('div', class_="a-section octopus-dlp-asin-title").text.replace('\n', '')
        
        info = [price,heading]
        thewriter.writerow(info)