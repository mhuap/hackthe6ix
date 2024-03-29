from flask import Flask, render_template, request, redirect
import sys
import geo

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def do_scrape(url, lang):
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    address1 = soup.h1.get_text()
    address2 = soup.h5.get_text()
    price = soup.h3.get_text()
    price_nums = int("".join(filter(str.isdigit, price)))
    rented = price_nums < 10000
    type = soup.find_all("span", class_="classifier")[3].get_text()
    description = soup.select('.property-description p.content')[0].get_text()

    address = address1 + ", " + address2
    if not 'Toronto' in address:
        return False
    if " - " in address:
        address = address[address.index(' - ') + 1:]

    address = address[:address.index(',') + 1] + ' Toronto, ON'
    house = str(type)

    return geo.process(address, rented, house, price, description, lang)

@app.route('/')
def home():
    language = request.args.get('lang')
    if not language:
        language = "en"
    return render_template('index.html', lang=language)

@app.route('/scrape', methods=['POST', 'GET'])
def result():
    language = request.args.get('lang')
    print(language)
    if not language:
        language = 'en'
    print(language, file=sys.stderr)
    if request.method == 'POST':
        url = request.form['url']
        if 'remax.ca' in url:
            info = do_scrape(url, language)
            if not info:
                return render_template('404.html', lang=language), 404
            else:
                return render_template('result.html', **info, posting=url, lang=language)
        else:
            return render_template('404.html', lang=language), 404
    else:
        return redirect("http://127.0.0.1:5000/", code=302)

if __name__ == '__main__':
 app.run()
