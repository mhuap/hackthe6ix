from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/scrape', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        return request.form['url']
    else:
        return "GET /scrape"

if __name__ == '__main__':
 app.run()
