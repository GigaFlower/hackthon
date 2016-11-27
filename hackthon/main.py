# -*- coding:utf-8 -*-
# Created by BigFlower at 16/11/26

import os
import json
from watson_developer_cloud import ToneAnalyzerV3


from flask import Flask, request, render_template

from .utility import photo_to_video

app = Flask(__name__, static_url_path='/root/hackthon/hackthon/website/')

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

tone_analyzer = ToneAnalyzerV3(username='a9b6615e-48b5-4a5e-9cfb-93b0163c44a2',password='y6z2NTmnBpND',version='2016-05-19')

@app.route('/tone', methods=['POST'])
def get_tone():
    string = request
    print(string)
    #return tone_analyzer.tone(text=string)
    
