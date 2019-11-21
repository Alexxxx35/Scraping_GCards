import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as request
from tqdm import tqdm
# soup=BeautifulSOup(html_doc,'html.parser')


my_url = 'https://www.newegg.com/global/fr-en/p/pl?d=graphic+cards'
Client = request(my_url)
page_html = Client.read()

page_soup = soup(page_html, "html.parser")

# print(page_soup.h1)
# print(page_soup.p)
# print(page_soup.body.span)

# print(products)
# print(len(products))
# print(products[0])

###definition of the product => item container
# container = products[0]
# print(container)
products = page_soup.findAll("div", {"class": "item-container"})
graphic_cards_data = []
graphic_cards_brands = []
graphic_cards_names = []
graphic_cards_ratings = []
graphic_cards_prices = []

for product in tqdm(products):
    all_product_brand = page_soup.find_all("a", {"class": "item-brand"})
    all_product_names = page_soup.find_all("a", {"class": "item-title"})
    all_product_rating = page_soup.find_all("a", {"class": "item-rating"})
    all_product_prices = page_soup.find_all("li", {"class": "price-current"})
    for product_brand in all_product_brand:
        graphic_cards_brands.append(product_brand.img['title'])
        # print(graphic_cards_brands)
    for product_name in all_product_names:
        graphic_cards_names.append(product_name.text)
        # print(graphic_cards_names)
    for product_rating in all_product_rating:
        graphic_cards_ratings.append(product_rating.i['class'][1])
        # if 'rating' in graphic_cards_ratings:
        #     print('yes')
        #     graphic_cards_ratings.remove('rating')
        # graphic_cards_ratings.remove('rating')
        # print(graphic_cards_ratings)
    for product_price in all_product_prices:
        graphic_cards_prices.append(product_price.strong.text+' euros')
        # print(graphic_cards_prices)
# tqdm(graphic_cards_data.extend((graphic_cards_brands, graphic_cards_names, graphic_cards_ratings, graphic_cards_prices)))
graphic_cards_data.append(graphic_cards_brands)
graphic_cards_data.append(graphic_cards_names)
graphic_cards_data.append(graphic_cards_ratings)
graphic_cards_data.append(graphic_cards_prices)
print(graphic_cards_data)

# print("rating: "+ product_rating)
# print("name: "+ product_name.text)
# print("price: "+ product_price.text)
Client.close()
