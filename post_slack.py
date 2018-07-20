
# -*- coding: utf-8 -*-
import os
import requests
import post_text


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
    post_text('sales_team', text)


post_slack()
