import requests
from bs4 import BeautifulSoup as BS
import json


# .productgrid--items.products-per-row-4
# https://www.petsy.online/collections/vegetarian-food-treats

# url = "https://www.petsy.online/collections/vegetarian-food-treats"
# r = requests.get(url)
# html = BS(r.content, "html.parser")

# print(html.select(".productgrid--items.products-per-row-4 > li"))

# items = html.select(".productitem")
# print(items)

# for el in html:
#     src = el.select(".productitem--image")
#     if src:
#         src = src[0].get("src")
#     title = el.select(".productitem--title > a")[0].text
#     company = el.select(".productitem--vendor > a")[0].text
#     price = el.select(".price__current price__current--emphasize.price__current--on-sale > .money")
#     if price:
#         price = price[0].text
#     print(src, title, company, price, sep="\n")



url = "https://www.bernpetfoods.co.uk/product-category/dog-food/?orderby=default"
r = requests.get(url)
html = BS(r.content, "html.parser")

# print(html.find_all(".ftc-product.product.variable"))
# print(html.select(".products.owl-carousel.style_1.loading"))
# print(html.select("#main-content"))
# ftc-product product
count = 0
for el in html.select("#main-content"):
    src = el.select(".attachment-shop_catalog.size-shop_catalog")[0].get("src")
    name = el.select(".product_title.product-name")[0].text
    price = el.select(".woocommerce-Price-amount.amount")[0].text
    count += 1
    print(src, "src",  name, "naem",  price)

print(count)