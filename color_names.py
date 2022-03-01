from bs4 import BeautifulSoup
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ( KHTML, like Gecko) '
                      'Chrome/94.0.4606.61 Safari/537.36 '
    }
url = 'https://www.macys.com/shop/womens-clothing/womens-tops?id=255'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
for items in soup.find_all('li', {"class": ["cell", "productThumbnailItem"]}):
    product_id_class = items.find(attrs={"class": ["productThumbnail", "redesignEnabled"]})
    product_id = product_id_class['id']
    # print(product_id, ":")
    try:
        num_of_colors = items.find('div', {"class": ["color-count", "hide-for-large"]}).text
        number_of_colors_available = int(num_of_colors[0])
        print("Colors available:", number_of_colors_available)
    except Exception as e:
        pass
    try:
        while number_of_colors_available > 0:
            li_color_swatch_class = items.find('li', {"class": "colorSwatch", "style": "background: inherit"}).html
            print(li_color_swatch_class)
            color_class = items.find('div', {"class": "swatchSelected"}).text
            print(color_class)
            # for all_colors in ul_color_swatch_class.find('li', {"class": "colorSwatch"}).div:
            #     color_title = all_colors['title']
            #     print("Color Name:", color_title)
            #     color_family = all_colors['data-colorswatchfamily']
            #     print("Color Family:", color_family)
            number_of_colors_available -= 1

    except Exception as e:
        pass