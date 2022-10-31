import requests

from requests.auth import HTTPBasicAuth

# r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))  # 简单写法
print(r.status_code)
