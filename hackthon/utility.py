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
    except Exception as e:
        return ''
    else:
        return resp.content


def wx_get_media(access_token, media_id):
    url = "https://api.weixin.qq.com/cgi-bin/media/get?access_token={}&media_id={}".format(access_token, media_id)
    try:
        resp = requests.get(url)
    except Exception as e:
        print("wx get media failed")
        print(e)
        return b''
    else:
        print("wx get media ret:")
        print(resp.content)
        return resp.content


def wx_put_media(access_token, data, media_type='voice'):
    url = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token={}&type={}".format(access_token, media_type)

    try:
        resp = requests.post(url, data)
    except Exception as e:
        print("wx get media failed")
        print(e)
        return b''
    else:
        print("wx get media ret:")
        print(resp.content)
        return resp.content


def photo_to_video(photo):
    emotion = emotion_api(photo)
    video = emotion_to_video(emotion)
    return video


def emotion_to_video(emotion):
    pass
