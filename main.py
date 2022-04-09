import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yarnplaza.com/'


def extract(*args):
    url = base_url + '/' + args[2]
    r = requests.get(url)
    if r.status_code != 200:
        r.raise_for_status()
    return (args[0], args[1], r.text)


def parse(*args):
    html = args[2]
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select('span.product-price-amount')[0].text
    
    data = {}
    data['name'] = args[0]
    data['item'] = args[1]
    data['price'] = price

    for item in soup.select('div#pdetailTableSpecs tr'):
        data[item.select('td')[0].text] = item.select('td')[1].text

    return data



items = [
        ('stylecraft', 'specialdk', 'yarn/stylecraft/stylecraft-special-dk'),
        ('DMC','natura xl', 'product/4216/dmc-natura-xl.html'),
        ('drops', 'safran', 'yarn/drops/drops-safran')
        ]

results = []
for item in items:
    html = extract(*item)
    results.append(parse(*html))

print(results)
