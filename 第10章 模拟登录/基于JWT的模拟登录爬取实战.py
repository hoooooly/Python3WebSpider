import requests
from urllib.parse import urljoin

from selenium import webdriver

BASE_URL = 'https://login3.scrape.center'
LOGIN_URL = urljoin(BASE_URL, '/api/login')
INDEX_URL = urljoin(BASE_URL, '/api/book')

USERNAME = 'admin'
PASSWORD = 'admin'

response_login = requests.post(LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD,
})

data = response_login.json()
print('Response json', data)

jwt = data.get('token')
print('JWT', jwt)

headers = {
    'Authorization': f'jwt {jwt}'
}

response_index = requests.get(INDEX_URL, params={
    'limit': 20,
    'offset': 0,
}, headers=headers)

print('Response Status', response_index.status_code)
print('Response Data', response_index.json())
