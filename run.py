from flask import Flask, render_template, request, jsonify
import sys

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

    return info

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
