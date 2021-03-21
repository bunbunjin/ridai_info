from bs4 import BeautifulSoup
import schedule
import requests


url = 'https://www.ous.ac.jp/'
res = requests.get(url)
html = BeautifulSoup(res.text, 'html.parser')
debag = html.find(class_='attention_on')
links = html.find(class_='attention_on').get_text()
link = html.find(class_='attention_on').find('a').get('href')
date = html.find(class_='attention_on').find('dt').get_text()


def info():
    res = requests.get(url)
    html = BeautifulSoup(res.text, 'html.parser')
    debag = html.find(class_='attention_on')
    links = html.find(class_='attention_on').get_text()
    link = html.find(class_='attention_on').find('a').get('href')
    date = html.find(class_='attention_on').find('dt').get_text()
    print('Get informe RIDAI newsg')
    return date, link, links
