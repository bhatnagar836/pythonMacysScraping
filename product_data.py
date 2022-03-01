from bs4 import BeautifulSoup
import requests
import math
import csv


def getting_each_item_details(soup):
    required_part = soup.find('ul', {"class": ["items", "grid-x", "small-up-2", "medium-up-3", "large-up-3"]})
    # print(required_part)
    count = 0
    i = 0
    list_section = required_part.find_all('li', {"class": ["cell", "productThumbnailItem"]})
    for items in list_section:
        product_id_class = items.find(attrs={"class": ["productThumbnail", "redesignEnabled"]})
        product_id = product_id_class['id']
        print(count, "]", product_id)

        # productDescLink
        product_url_class = items.find('a', {"class": "productDescLink"})['href']
        # print(product_url_class)
        product_url = f'''https://www.macys.com/{product_url_class}'''
        print("URL:", product_url)

        product_brand_class = items.find('div', {"class": "productBrand"}).text
        product_brand = product_brand_class.strip()
        # print(product_brand)
        product_title_class = items.find('a', {"class": "productDescLink"})['title']
        product_title = product_title_class.strip()
        # print(product_title)
        product_name = product_brand + " " + product_title
        print("Name:", product_name)

        try:
            product_price_class = items.find('span', {"class": ["regular", "originalOrRegularPriceOnSale"]}).text
            product_price = product_price_class.strip()
            print("Actual Price:", product_price)
        except Exception as e:
            pass

        try:
            product_sale_price_class = items.find('span', {"class": "regular"}).text
            product_sale_price = product_sale_price_class.strip()
            print("Sale Price:", product_sale_price)
        except Exception as e:
            pass

        try:
            num_of_colors = items.find('div', {"class": ["color-count", "hide-for-large"]}).text
            number_of_colors_available = num_of_colors[0]
            print("Colors available:", int(number_of_colors_available))
        except Exception as e:
            pass

        print("=======================================================================================")
        count += 1


def product_pages(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ( KHTML, like Gecko) '
                      'Chrome/94.0.4606.61 Safari/537.36 '
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_count = soup.find('p', {"class": "result-prod-count"}).text.strip()
    product_count = product_count.strip('(')
    product_count = int(product_count.strip(')'))
    print("product count =", product_count)
    page_count = product_count / 120
    actual_page_count = math.ceil(page_count)
    print("page_count =", actual_page_count)
    url_items = url.split("?")
    link_part = url_items[0]
    id_part = url_items[1]
    # print(url_items)

    current_page_count = 1
    while current_page_count <= actual_page_count:
        final_url = f'''{link_part}/Pageindex,Productsperpage/{current_page_count},120?{id_part}'''
        print(current_page_count, ")", final_url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ( KHTML, like Gecko) '
                          'Chrome/94.0.4606.61 Safari/537.36 '
        }

        response2 = requests.get(final_url, headers=headers)
        soup2 = BeautifulSoup(response2.content, 'html.parser')
        getting_each_item_details(soup2)
        current_page_count += 1
        break


# calling function
product_pages('https://www.macys.com/shop/womens-clothing/womens-tops?id=255')



