
# -*- coding: utf-8 -*- 
import os
import requests
import post_text
import json
import gspread
import oauth2client.client
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def get_events():
    # 認証
    json_key = json.load(open('credentials.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = oauth2client.client.SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
    gc = gspread.authorize(credentials)

    doc_id = '1cZw8ZG8Tgl5y8oKv27eRdFcvA4QpuRal0KlXmbrZvAQ'
    gfile   = gc.open_by_key(doc_id)
    wsheet  = gfile.get_worksheet(1) # シートのindexを任意で入力
    records = wsheet.get_all_records() # head=1を指定すると便利

    return records




def post_calender():
    records = get_events()
    div_slack_id = ""
    slack_id = ""
    date = ""
    time = ""

    for record in records:
        div_slack_id += record['div_slack_id']
        slack_id += records[0]['slack_id']
        date += records[0]['date']
        time += records[0]['time'] 

    
    # slackにポストする形式に整えた文章作成
    text = """ %s
今日も #techcamp-shibuya @ hereでリマインドよろしくお願いします。
以下のフォーマットに担当者のslackと各回のテーブルの番号を入力し、
BriefingのGyazoのリンクをその下にコピペして投稿してください。
Remindする時間:
    平日: 15:00
    土日祝: 12:00
```
【本日の説明会・体験会について】
時間: %s %s
担当: %s
来校予定のお客様：以下の写真をご参照ください！
体験会テーブル：
お忙しいと思いますが、ご協力お願いします！
この投稿とknowledgeを確認後、doneスタンプでリアクションをお願いします。
本日もよろしくお願いします！
Webサイト制作の体験会のアカウント: ID：html@tech-camp.in (pass:いつもの)
なお、カリキュラムは以下の通りです。
https://master.tech-camp.in/curriculums/2981
https://master.tech-camp.in/curriculums/2982
        ```"""%(div_slack_id, date, time, slack_id)
    post_text('test-naokada', text)
    #print(text)


post_calender()