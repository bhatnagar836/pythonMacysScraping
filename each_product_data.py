from sitemap_links import get_soup
import re
import csv

my_writer = csv.writer(open("product_category.csv", "w", newline=""))
header = ['Product_Id', 'Name', 'URL', 'Color Count', 'Regular Price', 'Sale Price']
my_writer.writerow(header)
def getting_each_item_details(url):
    each_page_soup = get_soup(url)
    # print(each_page_soup)
    # with open('readme.txt', 'w') as f:
    #     f.write(str(each_page_soup))
    required_part = each_page_soup.find('ul', {"class": "items"})
    # print(required_part)
    # with open('readme.txt', 'w') as f:
    #     f.write(str(each_page_soup))
    count = 0
    list_section = required_part.find_all('li', {"class": ["cell", "productThumbnailItem"]})
    for items in list_section:
        product_id_class = items.find(attrs={"class": ["productThumbnail", "redesignEnabled"]})
        product_id = product_id_class['id']
        print(count, "]", product_id)

        product_url_class = items.find('a', {"class": "productDescLink"})['href']
        # print(product_url_class)
        product_url = f'''https://www.macys.com/{product_url_class}'''
        print("URL:", product_url)

        try:
            num_of_colors = items.find('div', {"class": ["color-count", "hide-for-large"]}).text
            # print(num_of_colors)
            colour_count = num_of_colors.split(' ')
            # print(colour_count)
            number_of_colors_available = int(colour_count[0])
            print("Colors available:", number_of_colors_available)
        except Exception as e:
            pass

        product_brand_class = items.find('div', {"class": "productBrand"}).text
        product_brand = product_brand_class.strip()
        # print(product_brand)
        product_title_class = items.find('a', {"class": "productDescLink"})['title']
        product_title = product_title_class.strip()
        # print(product_title)
        product_name = product_brand + " " + product_title
        print("Name:", product_name)

        price_class = items.find('div', class_='priceInfo')

        def price_formatting(input_price):
            price_value = input_price.replace(',', '')
            # print(price_value)
            price_value = re.findall(r"[-+]?\d*\.\d+|\d+", price_value)[0]
            # print(price_value)
            return price_value

        try:
            product_price_class = price_class.find('span', {"class": ["regular", "originalOrRegularPriceOnSale"]}).text
            product_price = product_price_class.strip()
            product_price = price_formatting(product_price)
            print("Regular Price:", product_price)
        except Exception as e:
            pass

        try:
            product_sale_price_class = price_class.find('span', {"class": "discount"}).text
            product_sale_price = product_sale_price_class.strip()
            product_sale_price = price_formatting(product_sale_price)
            print("Sale Price:", product_sale_price)
        except Exception as e:
            pass
        print("=======================================================================================")
        count += 1
        my_writer.writerow([product_id, product_name, product_url, number_of_colors_available, product_price, product_sale_price ])
        # break


getting_each_item_details('https://www.macys.com/shop/womens-clothing/womens-tops/Pageindex,Productsperpage/1,120?id=255')