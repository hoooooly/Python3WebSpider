import requests
import re
import base64
import execjs

with open('./cookies1.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    ctx = execjs.compile(js_code).call('main123')
    print(ctx)

cookies = {
    'sucuri_cloudproxy_uuid_e26b4ac12': 'a369b18ec305b8057f1dffd5ae9a1138',
    '_ga': 'GA1.2.1433208535.1668434701',
    '_gid': 'GA1.2.1960652841.1668434701',
}

headers = {
    'authority': 'www.ontariogenomics.ca',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'sucuri_cloudproxy_uuid_e26b4ac12=a369b18ec305b8057f1dffd5ae9a1138; _ga=GA1.2.1433208535.1668434701; _gid=GA1.2.1960652841.1668434701',
    'cookie': ctx,
    'referer': 'https://www.ontariogenomics.ca/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

response = requests.get('https://www.ontariogenomics.ca/news-events/', headers=headers)
response = re.sub(r' ', '', response.content.decode('utf-8'))
String_data = re.findall("S='(.*?)'", response)[0]

# JS_Code = base64.b64decode(String_data).decode()
print(response.content.decode('utf-8'))
