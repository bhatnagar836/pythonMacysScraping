from sitemap_links import get_soup
import math
import csv


def product_pages(url):
    product_category_soup = get_soup(url)
    product_count = product_category_soup.find('p', {"class": "result-prod-count"}).text.strip()
    # print(product_count)
    product_count = product_count.strip('(')
    # print(product_count)
    product_count = int(product_count.strip(')'))
    # print(product_count)

    print("Total Products =", product_count)
    page_count = product_count / 120
    actual_page_count = math.ceil(page_count)
    print("page_count =", actual_page_count)
    url_items = url.split("?")
    link_part = url_items[0]
    id_part = url_items[1]
    print(url_items)

    current_page_count = 1
    while current_page_count <= actual_page_count:
        final_url = f'''{link_part}/Pageindex,Productsperpage/{current_page_count},120?{id_part}'''
        print(current_page_count, ")", final_url)
        current_page_count += 1
        break


# calling function
product_pages('https://www.macys.com/shop/womens-clothing/womens-tops?id=255')


