#!/usr/bin/env python3.10
import requests
from bs4 import BeautifulSoup

url_login = 'https://login.1c.ru/login'
url_cookies = 'https://login.1c.ru/user/profile'
url_data = 'https://dl02.1c.ru/public/file/get/b4a5112b-c85b-11e2-96f7-005056910018'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
}

data = {
    'email': '',
    'password': '',
    'rememberMe': 'on'
}

session = requests.Session()
session.headers.update(headers)
response = session.post(url_login, data=data, headers=headers)

print(response)
