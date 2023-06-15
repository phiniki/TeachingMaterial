# -*- coding: utf-8 -*-

from flask import Flask, render_template, make_response, request, redirect, send_file, url_for, send_from_directory

import pandas as pd

app = Flask(__name__)

page_dr = {
    "LoopContent":{"name":"繰り返し表示", "html":"LoopContent.html"},
    "ReadExcel_And_Show":{"name":"エクセル読み込み＆表示", "html":"ReadExcel_And_Show.html"},
}

@app.route('/', methods = ["GET"])
def index():

    response = make_response(render_template('index.html', page_dr=page_dr))
    return response

@app.route('/<string:page>/', methods = ["GET"])
def page(page):
    if page == "LoopContent":
        data = [
            {"title":"aa", "content":"aaaaaaaaaaaaaa"},
            {"title":"bb", "content":"bbbbbbbbbbbbbb"},
        ]
        response = make_response(render_template(page_dr[page]["html"], data=data))
        return response
    
    elif page == "ReadExcel_And_Show":
        df = pd.read_excel("input/ReadExcel_And_Show.xlsx")
        data = df.to_dict(orient='records')
        response = make_response(render_template(page_dr[page]["html"], data=data))
        return response

    response = make_response(render_template(page_dr[page]["html"], data=data))
    return response

app.run(host='localhost', port=8888, debug=True)