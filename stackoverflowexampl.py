import csv
import requests
from bs4 import BeautifulSoup

def getData(url_to_scrap='https://www.investing.com/currencies/eur-usd-historical-data', file=None, save_file="Name.csv"):

    if url_to_scrap is not None:
        header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(url_to_scrap, headers=header)  
        data = BeautifulSoup(r.content, 'html.parser')
    else:
        data = BeautifulSoup(open(file, encoding='utf8'), 'html.parser')


    table = data.find(id='curr_table')
    # table = table.find_all('td')

    print(table)

    # row_data = []
    # for row in table:
    #     row_data.append(row.get_text('data-real-value'))


    # with open(save_file, 'wb') as save:
    #     writer = csv.writer(save, delimiter=';')
    #     for row in [row_data[x:x+6] for x in range(0, len(row_data), 6)]:
    #         writer.writerow(row)


getData(save_file="EUR USD Historical Data.csv")