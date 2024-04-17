import requests
from bs4 import BeautifulSoup as BS
import json

# url = "https://www.dogster.com/category/dog-health-care"
# r = requests.get(url)
# html = BS(r.content, "html.parser")

# cards = []

# for el in html.select(".ast-row > article"):
#     src = el.select(".post-thumb-img-content.post-thumb > a > img")
#     if src:
#         src = src[0].get("data-lazy-src")
#     # href = el.select(".post-thumb-img-content > a")
#     title = el.select(".entry-title > a")[0].text
#     href = el.select(".entry-title > a")[0].get('href')
#     desc = el.select(".ast-excerpt-container.ast-blog-single-element > p")[0].text
#     cards.append({
#         'title': title,
#         'desc': desc,
#         'href': href,
#         'src': src
#     })
#     # cards.append([title, desc, href, src])


# json_cards = json.dumps(cards)


# print(json_cards)




# url = "https://basepaws.com/dog-breeds"
# r = requests.get(url)
# html = BS(r.content, "html.parser")

# cards = []




# for el in html.select(".catalog__card"):
#     href = el.get("href")
#     src = el.select(".media-card__img-wrap > img")[0].get("src")
#     name = el.select(".media-card__family")[0].text
#     desc = el.select(".media-card__breed")[0].text

#     cards.append({
#         'name': name,
#         'desc': desc,
#         'href': href,
#         'src': src
#     })
    
# print(cards)
