# -*- coding:utf-8 -*-
# Created by BigFlower at 16/11/26

import json, time
import requests

APP_ID = "wx95bf80d4527bc043"
APP_SECRET = "5cc438f21007cd3276e54529f17b1a9f"

TOKEN_MEMO = ['', 0]  # [<token>, <expire_at>]


def wx_get_access_token():
    if time.time() < TOKEN_MEMO[1]:
        return TOKEN_MEMO[0]

    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}" \
        .format(APP_ID, APP_SECRET)
    try:
        resp = requests.get(url)
    except Exception as e:
        print("wx get access token failed")
        print(e)
        return ''
    else:
        ret = json.loads(resp.text)
        TOKEN_MEMO[0] = ret['access_token']
        TOKEN_MEMO[1] = ret['expires_in'] + time.time()
        return TOKEN_MEMO[0]


def wx_get_media(media_id):
    try:
        access_token = wx_get_access_token()
        url = "https://api.weixin.qq.com/cgi-bin/media/get?access_token={}&media_id={}".format(access_token, media_id)
        resp = requests.get(url)
    except Exception as e:
        print("wx get media failed")
        print(e)
        return b''
    else:
        print("wx get media ret:")
        print(resp.content)
        return resp.content


def wx_put_media(data, media_type='voice'):
    try:
        access_token = wx_get_access_token()
        url = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token={}&type={}".format(access_token, media_type)
        resp = requests.post(url, data)
    except Exception as e:
        print("wx get media failed")
        print(e)
        return b''
    else:
        print("wx get media ret:")
        print(resp.content)
        return resp.content
