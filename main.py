# -*- coding: utf-8 -*-

from flask import Flask, render_template, make_response, request, redirect, send_file, url_for, send_from_directory

import pandas as pd

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def index():
    df = pd.read_excel("input/ReadExcel_And_Show.xlsx")
    data = df.to_dict(orient='records')

    response = make_response(render_template('index.html', data=data))
    return response

app.run(host='localhost', port=8888, debug=True)