# -*- coding:utf-8 -*-
# Created by BigFlower at 16/11/26

import json, http
import requests


def emotion_api(photo):
    try:
        resp = requests.post("https://api.projectoxford.ai/emotion/v1.0/recognize",
                             data=photo.read(),
                             headers={'Content-Type': 'application/octet-stream',
                                      'Ocp-Apim-Subscription-Key': '13b113fed5884aa998de124391a004f3',
                                      'Content-Length': '1280'
                                      }
                             )
        # conn = http.client.HTTPSConnection('api.projectoxford.ai')
        # conn.request("POST", "/emotion/v1.0/recognize", photo.read(), headers={
        #     'Content-Type': 'application/octet-stream',
        #     'Ocp-Apim-Subscription-Key': '13b113fed5884aa998de124391a004f3',
        # })
        # response = conn.getresponse()
        # resp = response.read()
        # print(resp)
        # conn.close()
        resp = json.loads(resp.text)
        if 'error' in resp:
            raise ValueError(resp['error'])

    except Exception as e:
        print(e)
        return ''
    else:
        return json.loads(resp.text)


def photo_to_video(photo):
    print("getting emotion...")
    emotion = emotion_api(photo)
    print("emotion:", emotion)
    video = emotion_to_video(emotion)
    return video


def emotion_to_video(emotion):
    return 'test.mp3'
