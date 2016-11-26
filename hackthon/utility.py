# -*- coding:utf-8 -*-
# Created by BigFlower at 16/11/26

import requests


def emotion_api(photo):
    try:
        resp = requests.post("https://api.projectoxford.ai/emotion/v1.0/recognize",
                             data=photo,
                             headers={'Content-Type': 'application/octet-stream',
                                      'Ocp-Apim-Subscription-Key': '13b113fed5884aa998de124391a004f3'}
                             )
        resp = resp.text
    except Exception as e:
        return ''
    else:
        return resp
