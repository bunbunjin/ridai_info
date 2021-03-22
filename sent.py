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


def check():
    while True:
        bef = info()
        time.sleep(3600)
        aft = info()
        if aft == bef:
            pass
        else:
            print("successfull")
            template = f'{aft()[2]}\n{aft()[1]}'
            line_massage(template)


check()
