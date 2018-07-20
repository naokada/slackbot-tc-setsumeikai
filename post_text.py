# -*- coding: utf-8 -*-
import os
import requests

def post_text(channel, text):

    """
    Slackの特定のチャンネルにtextを送信する
    """
    url_slack_api = 'https://slack.com/api/chat.postMessage'
    slack_api_params = {
        'token': os.environ.get('SLACKBOT_API_TOKEN','/home/username/'),
        'channel': channel,
        'text': text,  # 投稿するテキスト
        'username': 'setsumeikai-notify',  # 投稿のユーザー名
        'icon_emoji': ':robot_face:',  # 投稿のプロフィール画像に入れる絵文字
        'link_names': 1,  # メンションを有効にする
    }
    requests.post(url_slack_api, data=slack_api_params)
