# -*- coding:utf-8 -*-
# Created by BigFlower at 16/11/26

import os

from flask import Flask, request, render_template

from .utility import photo_to_video

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        try:
            photo = request.files['photo']
        except KeyError:
            return "'photo' file is required"
        else:

            photo.save(os.path.join('hackthon', 'static', 'photo','photo.jpg'))
            video_file_name = photo_to_video(photo)

            return render_template('index.html', photo='photo.jpg', music=video_file_name)
    else:
        return render_template('index.html', photo='', music='')


@app.route('/test', methods=['GET'])
def hello_world():
    return "如果你看到了本页面\n,那说明你有网"
