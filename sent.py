import requests
from scraping.info import info
import schedule
import time


def line_massage(line_massage_notification):
    token = ''
    line_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': f'message: {line_massage_notification}'}
    requests.post(line_api, headers=headers, data=data)


print(info())


def check():
    date_, link_, links_ = info()
    after = schedule.every(1).hours.do(info)
    before = schedule.every(5).minutes.do(info)
    schedule.run_pending()
    if after == before:
        print('前のデータと変わらない')
    else:
        print("successfull")
        print(f'{info()[0]}\n{info()[1]}')
        return date_, link_


while True:
    schedule.run_pending()

    time.sleep(3)
