from flask import Flask, render_template, request, jsonify
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

    
    address = address1 + ", " + address2
    if " - " in address:
        address = address[address.index(' - ') + 1:]

    address = address[:address.index(',') + 1] + ' Toronto, ON'
    price = int(price.replace('$', '').replace(',', ''))
    house = str(type)

    return geo.process(address, rented, house, price)

def calc_risk(info):
    risk = breakins/76

    if rented:
       risk *= 1.37
    if house:
       risk *= 1.42
    return risk


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        return render_template('result.html', **do_scrape(request.form['url']))
    else:
        return "Nope"

if __name__ == '__main__':
 app.run()
