import requests
from bs4 import BeautifulSoup

# def scrape_website(url):
#   response = requests.get(url)
#   soup = BeautifulSoup(response.content, 'html.parser')
#   data = soup.find_all('div', class_='product-info')
#   for product in data:
#     name = product.find('h4', class_='product-name').text
#     price = product.find('span', class_='product-price').text
#     print(name, price)

# if __name__ == '__main__':
#   url = 'https://www.amazon.com/s?k=books'
#   scrape_website(url)



import csv

# def scrape_website(url):
#   response = requests.get(url)
#   soup = BeautifulSoup(response.content, 'html.parser')
#   data = soup.find_all('div', class_='a-section')
#   with open('results.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for product in data:
#       name = product.find('span', class_='a-size-medium').text
#       price = product.find('span', class_='a-offscreen').text
#       author = product.find('span', class_='a-size-base').text
#       writer.writerow([name, price, author])

# if __name__ == '__main__':
#   url = 'https://www.amazon.com/s?k=books'
#   scrape_website(url)


def scrape_website(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  data = soup.find_all('div', class_='a-section')
  for product in data:
    name = product.find('img').get('alt')
    price = product.find('span', class_='a-price-whole').text
    print(name, price)

if __name__ == '__main__':
  url = 'https://www.amazon.com/s?k=books'
  scrape_website(url)