import requests
from bs4 import BeautifulSoup as bs
import csv

with open('newegg_macbooks.csv', 'a') as f:
    w = csv.writer(f)
    col_names = ['name', 'price', 'brand', 'series', 'model',
                 'rating', 'os', 'cpu_type', 'cpu_speed', 'cores',
                 'storage', 'memory', 'gpu_type', 'gpu_memory', 'screen']
    w.writerow(col_names)

    for p in range(8, 20):
        # track progress
        print('on page ' + str(p) + '...')
        print('~'*10)

        payload = {'api_key': '6f778a820ab7912beb310a1a4f021151',
                   'url': 'https://www.newegg.com/p/pl?d=macbook&Page=' + str(p)}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        page = requests.get('http://api.scraperapi.com', params=payload, headers=headers)
        soup = bs(page.text, 'html.parser')

        # loop through item info cards
        item_infos = soup.find_all(class_='item-info')[4:]
        for i in range(len(item_infos)):
            # track progress
            print('on product ' + str(i) + '...')

            # put info in dictionary
            product_info = {'Name': '', 'Price': '', 'Brand': '', 'Series': '', 'Model': '',
                            'Rating': '', 'Operating System': '', 'CPU Type': '', 'CPU Speed': '',
                            'Number of Cores': '',
                            'Storage': '', 'Memory': '', 'GPU/VPU': '', 'Video Memory': '', 'Screen Size': ''}

            # get name and price
            name = item_infos[i].find(class_='item-title').text.strip()
            if item_infos[i].find('li', class_='price-current').strong is not None:
                price = item_infos[i].find('li', class_='price-current').strong.text + \
                        item_infos[i].find('li', class_='price-current').sup.text
            else:
                price = ''
            product_info['Name'] = name
            product_info['Price'] = price


            # visit product page
            payload_2 = {'api_key': '6f778a820ab7912beb310a1a4f021151',
                         'url': item_infos[i].find('a', class_='item-title')['href']}
            page_2 = requests.get('http://api.scraperapi.com', params=payload_2, headers=headers)
            soup_2 = bs(page_2.text, 'html.parser')

            # get rating if it has one
            try:
                rating = soup_2.find('div', class_='grpRating').find('i', class_='rating')['title'][0]
                product_info['Rating'] = rating
            except AttributeError:
                pass
            except TypeError:
                pass

            # get specs
            for fieldset in soup_2.find_all('fieldset'):
                for dl in fieldset.find_all('dl'):
                    if dl.dt.text.strip() in product_info.keys():
                        product_info[dl.dt.text.strip()] = dl.dd.text.strip()

            # write to csv
            w.writerow(product_info.values())

# close the file
f.close()
