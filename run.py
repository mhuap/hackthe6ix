from flask import Flask, render_template, request, jsonify

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def do_scrape(url):
    page = requests.get("https://www.remax.ca/on/toronto-real-estate/23-pharmacy-ave-wp_id248682454-lst")
    soup = BeautifulSoup(page.content, 'html.parser')
    all = soup.find_all("h1", class_="address")

    return jsonify([x.prettify() for x in all])

@app.route('/scrape', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # return do_scrape(request.form['url'])
        return render_template('result.html', url=request.form['url'])
    else:
        return render_template('result.html', url='https://www.remax.ca/on/toronto-real-estate/23-pharmacy-ave-wp_id248682454-lst')

if __name__ == '__main__':
 app.run()
