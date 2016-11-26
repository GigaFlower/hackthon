# -*- coding:utf-8 -*-
# Created by BigFlower at 16/11/26

from flask import Flask, request, render_template

from .utility import emotion_api

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return "如果你看到了本页面\n,那说明你有网"


@app.route('/test', methods=['GET'])
def test():
    return render_template('index.html')


@app.route('/emotion', methods=['POST'])
def emotion():
    try:
        photo = request.files['photo']
    except KeyError:
        return "'photo' file is required"
    else:
        emo = emotion_api(photo)
        return emo, 200
