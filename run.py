from flask import Flask, render_template, request, redirect
import sys
import geo

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def do_scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    address1 = soup.h1.get_text()
    address2 = soup.h5.get_text()
    price = soup.h3.get_text()
    price_nums = int("".join(filter(str.isdigit, price)))
    rented = price_nums < 10000
    type = soup.find_all("span", class_="classifier")[3].get_text()
    description = soup.select('.property-description p.content')[0].get_text()

    info = {}
    info['address'] = address1 + ", " + address2
    info['price'] = price
    info['rented'] = "Rent" if rented else "Own"
    info['type'] = type.capitalize()
    info['description'] = description

    address = address1 + ", " + address2
    if " - " in address:
        address = address[address.index(' - ') + 1:]

    address = address[:address.index(',') + 1] + ' Toronto, ON'
    price = int(price.replace('$', '').replace(',', ''))
    house = str(type)

    return geo.process(address, rented, house, price)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        url = request.form['url']
        if 'remax.ca' in url:
            return render_template('result.html', **do_scrape(url))
        else:
            return render_template('404.html'), 404
    else:
        return redirect("http://127.0.0.1:5000/", code=302)

if __name__ == '__main__':
 app.run()
