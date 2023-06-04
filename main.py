import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint

payloads = {'page': 1}
url = 'https://santaesperanza.ge/categories/მხატვრული-ლიტერატურა/'
h = {'Accept-Language': 'en-US'}
file = open('books.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['title', 'desc', 'price'])

while payloads['page'] < 120:
    response = requests.get(url, params=payloads, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    book_soup = soup.find('div', class_='row', id='scrollproducts')
    all_books = book_soup.find_all('div', class_='col-6')
    for book in all_books:
        title = book.h5.text
        desc = book.find('div', class_='card-text').text
        price = book.find('span', class_='text-md').text
        print(title, desc, price)
        csv_obj.writerow([title, desc, price])
        payloads['page'] += 1
        sleep(randint(10, 20))

file.close()
