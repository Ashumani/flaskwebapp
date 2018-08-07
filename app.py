import json

import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """
        Getting news data from cryto compare api and displaying it on ui
    :return:
    """
    response = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    dict_app = json.loads(response.content) # json.loads convert json data into python dict

    return render_template('index.html', contents=dict_app['Data'])


if __name__ == '__main__':
    app.run()
