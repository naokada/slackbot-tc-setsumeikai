
# -*- coding: utf-8 -*-
import os
import requests


def post_slack():
    
    # slackにポストする形式に整えた文章作成
    text = """今日も #techcamp-shibuya でリマインドよろしくお願いします。
以下のフォーマットに担当者のslackと各回のテーブルの番号を入力し、
BriefingのGyazoのリンクをその下にコピペして投稿してください。
Remindする時間:
    平日: 15:00
    土日祝: 12:00
```
@here
【本日の説明会・体験会について】
担当:
来校予定のお客様：以下の写真をご参照ください！
体験会テーブル：
お忙しいと思いますが、ご協力お願いします！
この投稿とknowledgeを確認後、doneスタンプでリアクションをお願いします。
本日もよろしくお願いします！
Webサイト制作の体験会のアカウント: ID：html@tech-camp.in (pass:いつもの)
なお、カリキュラムは以下の通りです。
https://master.tech-camp.in/curriculums/2981
https://master.tech-camp.in/curriculums/2982
        ```"""
    post_text('test-naokada', text)

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

post_slack()
