# -*- coding:utf-8 -*-
# Created by BigFlower at 16/11/26

import json
import requests


def emotion_api(photo):
    try:
        resp = requests.post("https://api.projectoxford.ai/emotion/v1.0/recognize",
                             data=photo,
                             headers={'Content-Type': 'application/octet-stream',
                                      'Ocp-Apim-Subscription-Key': '13b113fed5884aa998de124391a004f3'}
                             )
    except Exception as e:
        print(e)
        return ''
    else:
        return json.loads(resp.text)


def photo_to_video(photo):
    emotion = emotion_api(photo)
    video = emotion_to_video(emotion)
    return video


def emotion_to_video(emotion):
    with open('music/test.mp3', 'rb') as f:
        return f.read()
