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
liste = []

for product in tqdm(products):
    all_product_brand = page_soup.find_all("a", {"class": "item-brand"})
    all_product_names = page_soup.find_all("a", {"class": "item-title"})
    all_product_rating = page_soup.find_all("a", {"class": "item-rating"})
    all_product_prices = page_soup.find_all("li", {"class": "price-current"})

    for j, prod in enumerate(all_product_names):
        p = {}
        p["name"] = all_product_names[j].text.strip()
        p["brand"] = all_product_brand[j].img['title'] if len(all_product_brand) > j else ""
        p["rating"] = all_product_rating[j].i['class'][1] if len(all_product_rating) > j else ""
        p["price"] = all_product_prices[j].strong.text + ' euros' if len(all_product_prices) > j else ""
        liste.append(p)
print(liste)
Client.close()
