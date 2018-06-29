
# -*- coding: utf-8 -*-
import os
import requests


def post_slack():
    
    # slackにポストする形式に整えた文章作成
    text = '今日も#techcamp-shibuyaでリマインドよろしくお願いします。\n以下のフォーマットに***担当者のslack***と***各回のテーブルの番号***を入力し、BriefingのGyazoのリンクをその下にコピペして投稿してください。\n```\n@here\n【本日の説明会・体験会について】\n担当: \n来校予定のお客様：以下の写真をご参照ください！\n体験会テーブル：\nお忙しいと思いますが、ご協力お願いします！\n本日もよろしくお願いします！\n```'
    post_text('test-naokada', text)

def post_text(channel, text):

    """
    Slackの特定のチャンネルにtextを送信する（未検証メソッド）
    """
    print os.environ.has_key("SLACKBOT_API_TOKEN")

    # Shows env variables
    for k, v in os.environ.items():
        print("{key} : {value}".format(key=k, value=v))

    url_slack_api = 'https://slack.com/api/chat.postMessage'
    slack_api_params = {
        'token': os.environ.get('SLACKBOT_API_TOKEN','/home/username/'),
        'channel': channel,
        'text': text,  # 投稿するテキスト
        'username': 'setsumeikai-notify',  # 投稿のユーザー名
        'icon_emoji': ':sunglasses:',  # 投稿のプロフィール画像に入れる絵文字
        'link_names': 1,  # メンションを有効にする
    }
    requests.post(url_slack_api, data=slack_api_params)

post_slack()