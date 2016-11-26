# -*- coding:utf-8 -*-
# Created by BigFlower at 16/11/26

from flask import Flask, request, render_template

from .utility import emotion_api, photo_to_video
from .wx_utility import wx_get_media, wx_put_media
from .wxreceive import parse_xml, Msg
from .wxreply import VideoMsg

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return "如果你看到了本页面\n,那说明你有网"


# def wx_verify():
#     echostr = request.args.get('echostr')
#     return echostr
#

@app.route('/wx', methods=['GET'])
def wx_handle():
    try:
        data = request.data
        print("Handle Post webdata is ", data)
        msg = parse_xml(data)
        if isinstance(msg, Msg):
            toUser = msg.FromUserName
            fromUser = msg.ToUserName
            # if msg.MsgType == 'text':
            #     content = "test"
            #     return rTextMsg(toUser, fromUser, content).send()
            assert msg.MsgType == 'image'
            media_id = msg.MediaId
            media = wx_get_media(media_id)
            video = photo_to_video(media)
            video_id = wx_put_media(video, media_type='voice')['media_id']
            return VideoMsg(toUser, fromUser, video_id).send()
            # else:
            #     print("Unknown msg type")
            #     return "success"
        else:
            print("暂且不处理")
            return "success"
    except Exception as e:
        return e


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
