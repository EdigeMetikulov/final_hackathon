import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.nyxcosmetic.ru/more"


def get_html(url):
    responce = requests.get(url)
    return responce.text  # отправляем запрос на сайт и получаем просто html текст страницы


def get_soup(html):
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_last_page_number(soup):
    pagination_list = soup.find("ul", class_="items pages-items").find_all("li")
    item = pagination_list[-2]
    last = item.find("a").findAll('span')
    last = last[1].text
    return int(last)


def get_product_cards(soup):
    product_list = soup.find("ol", class_="products")
    products = product_list.find_all("li", class_="item")
    return products


def get_category(soup):
    all_categories = soup.find("div", class_="page-title-wrapper")
    category = all_categories.find("span", class_="base").text
    return category


def get_data_from_cards(products, category, id=1):
    import random
    for product in products:
        try:
            title = product.find("a", class_='product-item-link').text
            # print(title)
        except:
            title = ""
        try:
            desc = product.find("a", class_="product").text.strip()
            # print(desc)
        except:
            desc = ""

        random_price = random.randint(1000, 5000)
        price = round(random_price)
        try:
            # image = product.find('img', class_="product-image-photo lazy lazy_loaded").get('src')
            image = product.find("a").find("span").find('img').get('data-src')
            # print(image)
        except:
            image = "sorry"
        id += 1
        create_date = "2022-06-16 17:03:20.779634+06"
        update_date = "2022-06-16 17:03:20.779634+06"
        watch = 0
        is_published = 't'
        data = {"id": id, "title": title, "desc": desc, 'category': category, 'price': price, "image": image,
                "create_date": create_date, "update_date": update_date, "is_published": is_published, "watch": watch}
        # print(data)
        write_to_scv(data)
        # save_data(data)
    return id


# copy product_product from '/home/edige/PycharmProjects/django_learn/final_hackathon/apps/parsing/nyxcosmetic.csv' delimiter '|' csv header;

def write_to_scv(data):
    with open("nyxcosmetic.csv", "a") as file:
        writer = csv.writer(file, delimiter="|")
        writer.writerow((data["id"], data["title"], data["desc"], data["category"], data["price"], data["image"],
                         data["create_date"], data["update_date"], data["is_published"], data["watch"],))


def main():
    html = get_html(url)
    soup = get_soup(html)
    category = get_category(soup)
    last_page_num = get_last_page_number(soup)
    id = 6
    for page in range(1, last_page_num + 1):
        page_url = url + "?p=" + str(page)
        print(page_url)
        html = get_html(page_url)
        soup = get_soup(html)
        cards = get_product_cards(soup)
        id = get_data_from_cards(cards, category, id)

