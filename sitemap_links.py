from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ( KHTML, like Gecko) '
                  'Chrome/94.0.4606.61 Safari/537.36 '
}

url = 'https://www.macys.com/shop/sitemap-index?id=199462'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
required_section = soup.find('div', class_='htmlSnippet')
# print(required_section)

my_writer = csv.writer(open("SiteMap_links.csv", "w", newline=""))
header = ['Product_Name', 'Product_Link']
my_writer.writerow(header)

products_links_list = []
for output in required_section.find_all('a', href=True):
    product_category = output.text
    # print(product_category)
    product_links = output['href']
    # print(product_links)
    # print(product_category, ":", product_links)
    products_links_list.append(product_links)
    my_writer.writerow([product_category, product_links])
print(products_links_list)

