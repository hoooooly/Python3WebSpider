"""思路
遍历所有页码，构造10页的索引页URL
从每个索引页，分析提取出每个电影的详情页URL"""

import requests
import logging
import re
import json
from urllib.parse import urljoin
from os.path import exists
from os import makedirs

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
RESULT_DIR = 'results'
exists(RESULT_DIR) or makedirs(RESULT_DIR)


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

def scrape_page(url):
    logging.info('开始抓取 %s ...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('获取网页%s状态码: %s错误', url, response.status_code)
    except requests.exceptions.RequestException:
        logging.error('网页无法访问： %s', url, exc_info=True)  # 打印错误堆栈信息


def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    """解析详情页地址"""
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('详情页地址：%s', detail_url)
        yield detail_url


def scrape_detail(url):
    """详情页信息"""
    return scrape_page(url)


def parse_detail(html):
    """解析详情页"""
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
    categories_pattern = re.compile(
        '<div.*?"categories.*?<button.*?<span>(.*?)</span>.*?<button.*?<span>(.*?)</span>.*?</button>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映', re.S)
    drama_pattern = re.compile('<div.*?class="drama".*?</h3>.*?<p.*?>(.*?)</p.*?/div>', re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)

    cover = re.search(cover_pattern, html).group(1).strip() if re.search(categories_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else None
    published_at = re.search(published_at_pattern, html).group(1).strip() if re.search(published_at_pattern,
                                                                                       html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = re.search(score_pattern, html).group(1).strip() if re.search(score_pattern, html) else None

    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at_pattern': published_at,
        'drama': drama,
        'score': score
    }


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        details_urls = parse_index(index_html)
        for details_url in details_urls:
            details_html = scrape_detail(details_url)
            data = parse_detail(details_html)
            save_data(data)
            logging.info("电影详情：%s 保存成功", data)


if __name__ == '__main__':
    main()
    # index_html =  scrape_index('1')
    # details_urls = parse_index(index_html)
    # print(list(details_urls))
