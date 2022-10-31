import requests
import logging

logging.captureWarnings(True)
res = requests.get('https://ssr2.scrape.center/', verify=False)
print(res.status_code)
